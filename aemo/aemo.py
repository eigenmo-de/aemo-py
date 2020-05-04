from typing import List, Dict, Any, Iterable
import datetime as dt
import dateutil.parser as du
import pathlib as pl
import csv
import io

import aemo.key as key


class Table:
    _rows: List[Any]  # we verify that the data added matches the key
    _key: key.TableKey

    def __init__(self, row: List[str]):
        self._key = key.TableKey.from_row(row)
        self._rows = [self._mapping[self._key](row)]

    def add_row(self, row: List[str]) -> None:
        row_key = key.TableKey.from_row(row)
        if row_key == self._key:
            self._rows.append(self._mapping[row_key](row))
        else:
            raise key.TableRowsMustHaveSameKey()

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
    _original_name: str
    _data_source: str
    _creation_timestamp: dt.datetime
    _file_index: int
    _audience: str
    _desired_rows: int
    _files: Dict[key.TableKey, Table]

    @property
    def original_name(self) -> str:
        return self._original_name

    @property
    def data_source(self) -> str:
        return self._data_source

    @property
    def files(self) -> Dict[key.TableKey, Table]:
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
        for idx, row in enumerate(csv_reader):
            rowtype = row[0]
            if rowtype == "C":
                if idx == 0:  # first row
                    self._data_source = row[1]
                    self._creation_timestamp = du.parse(
                            row[5] + " " + row[6], dayfirst=True
                    )
                    self._audience = row[4]
                    self._participant = row[3]

                elif row[1] == "END OF REPORT":
                    self._desired_rows = int(row[2])
                    if (idx + 1) != self._desired_rows:
                        raise InvalidNumberOfRows(
                            "got {got} but expected {exp}"
                            .format(got=idx+1, exp=self._desired_rows)
                        )
                else:
                    raise UnexpectedRow(row)
            elif rowtype == "I":
                current_key = key.TableKey.from_row(row)
            elif rowtype == "D":
                if current_key is not None:
                    table = self._files.get(current_key)
                    if table is not None:
                        table.add_row(row)
                        self._files[current_key] = table
                    else:
                        self._files[current_key] = Table(row)
                else:
                    raise UnexpectedRow(row)
            else:
                raise UnexpectedRow(row)
        num_files = len(self._files)
        total_file_rows = sum([len(v) for v in self._files.values()])
        got_rows = total_file_rows + num_files + 2
        if got_rows != self._desired_rows:
            raise InvalidNumberOfRows(
                "got {got} but expected {exp}"
                .format(got=got_rows, exp=self._desired_rows)
            )
