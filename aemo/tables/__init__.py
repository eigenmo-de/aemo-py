import aemo.tables.settlements as settlements
from typing import Callable, Any, List
import aemo.key as key


# this needs to be updated as move modules are added above
def mapping(key: key.TableKey) -> Callable[[List[str]], Any]:
    to_fn = {

        # start settlements
        settlements.Cpdata.key():
        settlements.Cpdata.from_row,
        settlements.FcasRecovery.key():
        settlements.FcasRecovery.from_row,
        settlements.Marketfees.key():
        settlements.Marketfees.from_row,
        settlements.NmasRecovery.key():
        settlements.NmasRecovery.from_row,
        # end settlements

    }
    return to_fn[key]
