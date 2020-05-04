from aemo.tables.settlements import *

# this needs to be updated as move modules are added above
def mapping(key: key.TableKey) -> Callable[[List[str]], Any]:
    to_fn = {

        # start settlements
        Cpdata5.key():
        Cpdata5.from_row,
        FcasRecovery6.key():
        FcasRecovery6.from_row,
        Marketfees5.key():
        Marketfees5.from_row,
        NmasRecovery2.key():
        NmasRecovery2.from_row,
        # end settlements

    }
    return to_fn[key]
