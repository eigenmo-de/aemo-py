from typing import List, Dict, Any, Iterable
import datetime as dt
import pathlib as pl
import csv
import io

# we want these to be accessible from the root, eg aemo.TableKey
from aemo.key import TableKey, TableRowsMustHaveSameKey

# all tables themselves have unique names but are then re-exported via tables
import aemo.tables as tab


class Table:
    _rows: List[Any]  # we verify that the data added matches the key
    _key: TableKey

    def __init__(self, row: Any):
        self._key = row.key()
        self._rows = [row]

    def add_row(self, row: Any) -> None:
        row_key = row.key()
        if row_key == self._key:
            self._rows.append(row)
        else:
            raise TableRowsMustHaveSameKey()

    def __len__(self) -> int:
        return len(self._rows)

    @property
    def rows(self) -> List[Any]:
        return self._rows


class UnexpectedRow(Exception):
    pass


class InvalidNumberOfRows(Exception):
    pass


class NemFile:
    _data_source: str
    _creation_timestamp: dt.datetime
    _audience: str
    _desired_rows: int
    _files: Dict[TableKey, Table]
    _unsupported_files: Dict[TableKey, int]

    @property
    def data_source(self) -> str:
        return self._data_source

    @property
    def creation_timestamp(self) -> dt.datetime:
        return self._creation_timestamp

    @property
    def audience(self) -> str:
        return self._audience

    @property
    def desired_rows(self) -> int:
        return self._desired_rows

    @property
    def files(self) -> Dict[TableKey, Table]:
        return self._files

    @staticmethod
    def from_filesystem(path: pl.Path) -> "NemFile":
        with open(path, 'r') as f:
            return NemFile(csv.reader(f))

    @staticmethod
    def from_str(f: str) -> "NemFile":
        return NemFile(csv.reader(io.StringIO(f)))

    def __init__(self, csv_reader: Iterable[List[str]]) -> None:
        current_key = None
        self._files = dict()
        self._unsupported_files = dict()
        for idx, row in enumerate(csv_reader):
            rowtype = row[0]
            if rowtype == "C":
                if idx == 0:  # first row
                    self._data_source = row[1]
                    self._creation_timestamp = dt.datetime.strptime(
                        row[5] + " " + row[6],
                        "%Y/%m/%d %H:%M:%S"
                    )
                    self._audience = row[4]
                    self._participant = row[3]

                elif row[1] == "END OF REPORT":
                    self._desired_rows = int(row[2])
                else:
                    raise UnexpectedRow(row)
            elif rowtype == "I":
                current_key = TableKey.from_row(row)
            elif rowtype == "D":
                if current_key is not None:
                    if not current_key.row_matches(row):
                        raise TableRowsMustHaveSameKey

                    try:
                        table = self._files.get(current_key)
                        parsed = tab.mapping(current_key)(row)
                        if table is not None:
                            table.add_row(parsed)
                            self._files[current_key] = table
                        else:
                            self._files[current_key] = Table(parsed)
                    except KeyError:
                        # table not supported
                        # keep a set of all those unsupported
                        self._unsupported_files[current_key] = self._unsupported_files.get(current_key, 0) + 1
                else:
                    raise UnexpectedRow(row)
            else:
                raise UnexpectedRow(row)
        num_files = len(self._files)
        num_unsupported_files = len(self._unsupported_files)
        total_file_rows = sum([len(v) for v in self._files.values()])
        total_unsupported_rows = sum([v for v in self._unsupported_files.values()])
        got_rows = total_file_rows + num_files + 2 + total_unsupported_rows + num_unsupported_files
        if got_rows != self._desired_rows:
            raise InvalidNumberOfRows(
                "got {got} but expected {exp}"
                .format(got=got_rows, exp=self._desired_rows)
            )
