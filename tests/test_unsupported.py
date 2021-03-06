from context import aemo


def FILE_WITH_UNSUPPORTED():
    return """C,SETP.WORLD,SETTLEMENTS,AEMO,TESTCPY,2025/12/31,02:01:00,123456,SETTLEMENTS,123456,,,,,,,,,,,,,,,,,,,,,
I,SETTLEMENTS,NMAS_RECOVERY,2,SETTLEMENTDATE,VERSIONNO,PERIODID,PARTICIPANTID,SERVICE,CONTRACTID,PAYMENTTYPE,REGIONID,RBF,PAYMENT_AMOUNT,PARTICIPANT_ENERGY,REGION_ENERGY,RECOVERY_AMOUNT,LASTCHANGED,PARTICIPANT_GENERATION,REGION_GENERATION,RECOVERY_AMOUNT_CUSTOMER,RECOVERY_AMOUNT_GENERATOR,,,,,,,,,
D,SETTLEMENTS,NMAS_RECOVERY,2,2025/12/31 00:00:00,1,1,TESTCPY,RESTART,XYZ123,AVAILABILITY,TAS1,1.1,1.1,1.1,1.1,1.1,2025/12/31 02:01:00,1.1,1.1,1.1,1.1,,,,,,,,,
I,SETTLEMENTS,CPDATA,5,SETTLEMENTDATE,VERSIONNO,PERIODID,PARTICIPANTID,TCPID,REGIONID,IGENERGY,XGENERGY,INENERGY,XNENERGY,IPOWER,XPOWER,RRP,EEP,TLF,CPRRP,CPEEP,TA,EP,APC,RESC,RESP,METERRUNNO,HOSTDISTRIBUTOR,MDA,LASTCHANGED,METERDATA_SOURCE
D,SETTLEMENTS,CPDATA,5,2025/12/31 00:00:00,1,1,TESTCPY,ABCD,TAS1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,,,,1,,MSATS,2025/12/31 02:01:00,
I,SETTLEMENTS,FCAS_RECOVERY,6,SETTLEMENTDATE,VERSIONNO,PARTICIPANTID,REGIONID,PERIODID,LOWER6SEC_RECOVERY,RAISE6SEC_RECOVERY,LOWER60SEC_RECOVERY,RAISE60SEC_RECOVERY,LOWER5MIN_RECOVERY,RAISE5MIN_RECOVERY,LOWERREG_RECOVERY,RAISEREG_RECOVERY,LASTCHANGED,LOWER6SEC_RECOVERY_GEN,RAISE6SEC_RECOVERY_GEN,LOWER60SEC_RECOVERY_GEN,RAISE60SEC_RECOVERY_GEN,LOWER5MIN_RECOVERY_GEN,RAISE5MIN_RECOVERY_GEN,LOWERREG_RECOVERY_GEN,RAISEREG_RECOVERY_GEN,,,,,
D,SETTLEMENTS,FCAS_RECOVERY,6,2025/12/31 00:00:00,1,TESTCPY,TAS1,1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,2025/12/31 02:01:00,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,,,,,
I,SETTLEMENTS,MARKETFEES,5,SETTLEMENTDATE,RUNNO,PARTICIPANTID,PERIODID,MARKETFEEID,MARKETFEEVALUE,ENERGY,LASTCHANGED,PARTICIPANTCATEGORYID,,,,,,,,,,,,,,,,,,
D,SETTLEMENTS,MARKETFEES,5,2025/12/31 00:00:00,1,TESTCPY,1,V_EST,1.1,1.1,2025/12/31 02:01:00,XYZ,,,,,,,,,,,,,,,,,,
I,SETTLEMENTS,UNSUPPORTED_DATA,3,SETTLEMENTDATE,VERSIONNO
D,SETTLEMENTS,UNSUPPORTED_DATA,3,2025/12/31 00:00:00,1
D,SETTLEMENTS,UNSUPPORTED_DATA,3,2025/12/31 00:01:00,1
D,SETTLEMENTS,UNSUPPORTED_DATA,3,2025/12/31 00:02:00,1
C,END OF REPORT,14,,,,,,,,,,,,,,,,,,,,,,,,,,,,"""


def test_parse_file_with_unsupported():
    _ = aemo.NemFile.from_str(FILE_WITH_UNSUPPORTED())
