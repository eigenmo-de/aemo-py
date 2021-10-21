import aemo.tables.settlements as settlements
from typing import Callable, Any, List
import aemo.key as key


# this needs to be updated as move modules are added above
def mapping(key: key.TableKey) -> Callable[[List[str]], Any]:
    to_fn = {
        # start settlements
        settlements.DayTrack.key().unversioned(): settlements.DayTrack.from_row,
        settlements.Cpdata.key().unversioned(): settlements.Cpdata.from_row,
        settlements.FcasRecovery.key().unversioned(): settlements.FcasRecovery.from_row,
        settlements.Marketfees.key().unversioned(): settlements.Marketfees.from_row,
        settlements.NmasRecovery.key().unversioned(): settlements.NmasRecovery.from_row,
        settlements.Reallocations.key().unversioned(): settlements.Reallocations.from_row,
        # end settlements
    }
    return to_fn[key.unversioned()]
