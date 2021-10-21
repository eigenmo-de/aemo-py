from dataclasses import dataclass
from typing import List, Tuple


@dataclass(
    init=True,
    frozen=True,
)
class TableKey:
    collection: str
    name: str
    version: int

    @staticmethod
    def from_row(row: List[str]) -> "TableKey":
        return TableKey(collection=row[1], name=row[2], version=int(row[3]))

    def row_matches(self, row: List[str]) -> bool:
        return self == TableKey.from_row(row)

    def format(self) -> str:
        return "{coll}-{name}-v{ver}".format(
            coll=self.collection,
            name=self.name,
            ver=self.version
        )

    def unversioned(self) -> Tuple[str, str]:
        return (self.collection, self.name)


class TableRowsMustHaveSameKey(Exception):
    pass
