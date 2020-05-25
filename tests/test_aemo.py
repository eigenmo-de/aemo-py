from context import aemo
import datetime as dt
import csv
import io


def ROW_CPDATA_1():
    return list(csv.reader(io.StringIO("""D,SETTLEMENTS,CPDATA,5,2025/12/31 00:00:00,1,1,TESTCPY,ABCD,TAS1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,,,,1,,MSATS,2025/12/31 02:01:00,""")))[0]


def ROW_CPDATA_2():
    return list(csv.reader(io.StringIO("""D,SETTLEMENTS,CPDATA,5,2025/12/31 00:00:00,1,2,TESTCPY,ABCD,TAS1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,,,,1,,MSATS,2025/12/31 02:01:00,""")))[0]


def ROW_FCAS_3():
    return list(csv.reader(io.StringIO("""D,SETTLEMENTS,FCAS_RECOVERY,6,2025/12/31 00:00:00,1,TESTCPY,TAS1,1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,2025/12/31 02:01:00,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,,,,,""")))[0]


def BASIC_FILE():
    return """C,DATA.SET,SOMEDATA,AEMO,TESTCPY,2025/12/31,02:01:00,123456,SOMEDATA,123456
C,END OF REPORT,2,,,,,,"""


def desired_key() -> aemo.TableKey:
    return aemo.TableKey(
        collection="SETTLEMENTS",
        name="CPDATA",
        version=5,
        )


# test aemo.NemFile
# verify properties are extracted correctly from file
def test_file_extract_properties():
    parsed = aemo.NemFile.from_str(BASIC_FILE())
    assert parsed.data_source == "DATA.SET"
    assert parsed.files == {} 
    assert parsed.creation_timestamp == dt.datetime(2025, 12, 31, 2, 1, 0)
    assert parsed.desired_rows == 2
    assert parsed.audience == "TESTCPY"


def test_key():
    row_1_key = aemo.TableKey.from_row(ROW_CPDATA_1())
    row_2_key = aemo.TableKey.from_row(ROW_CPDATA_2())
    row_3_key = aemo.TableKey.from_row(ROW_FCAS_3())
    assert row_1_key == desired_key()
    assert row_2_key == desired_key() 
    assert row_3_key != desired_key()
    assert desired_key().row_matches(ROW_CPDATA_1())
    assert desired_key().row_matches(ROW_CPDATA_2())
    assert (not desired_key().row_matches(ROW_FCAS_3()))


def test_table_wrong_key():
    parsed1 = aemo.tables.mapping(aemo.TableKey.from_row(ROW_CPDATA_1()))(ROW_CPDATA_1())
    parsed2 = aemo.tables.mapping(aemo.TableKey.from_row(ROW_CPDATA_2()))(ROW_CPDATA_2())
    parsed3 = aemo.tables.mapping(aemo.TableKey.from_row(ROW_FCAS_3()))(ROW_FCAS_3())

    cp_table = aemo.Table(parsed1)

    # test that Table(row) - creates a table with the correct key
    assert cp_table._key == aemo.TableKey.from_row(ROW_CPDATA_1())

    fc_table = aemo.Table(parsed3)

    # test that Table(row) - creates a table with the correct key
    assert fc_table._key == aemo.TableKey.from_row(ROW_FCAS_3())

    assert len(cp_table) == 1

    cp_table.add_row(parsed2)

    assert len(cp_table) == 2

    assert cp_table.rows == [parsed1, parsed2]

    # verify that it is impossible to add a row with incorrect table key
    try:
        cp_table.add_row(parsed3)
    except aemo.TableRowsMustHaveSameKey:
        assert True
    except Exception:
        assert False

    # verify that it is impossible to add a row with incorrect table key
    try:
        fc_table.add_row(parsed1)
    except aemo.TableRowsMustHaveSameKey:
        assert True
    except Exception:
        assert False
