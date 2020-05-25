import aemo.tables.settlements as settlements
from typing import Callable, Any, List
import aemo.key as key


# this needs to be updated as move modules are added above
def mapping(key: key.TableKey) -> Callable[[List[str]], Any]:
    to_fn = {

        # start settlements
        settlements.Cpdata5.key():
        settlements.Cpdata5.from_row,
        settlements.FcasRecovery6.key():
        settlements.FcasRecovery6.from_row,
        settlements.Marketfees5.key():
        settlements.Marketfees5.from_row,
        settlements.NmasRecovery2.key():
        settlements.NmasRecovery2.from_row,
        # end settlements

    }
    return to_fn[key]
