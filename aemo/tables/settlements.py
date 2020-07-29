from typing import List, Optional
import datetime as dt
import aemo.key as key

from dataclasses import dataclass
import decimal

# can throw ValueError due to date parsing


def opt_decimal(s: str) -> Optional[decimal.Decimal]:
    if s == "":
        return None
    else:
        return decimal.Decimal(s)


@dataclass(frozen=True)
class DayTrack:
    settlementdate: dt.date
    expostrunno: decimal.Decimal
    lastchanged: dt.datetime

    @staticmethod
    def key() -> key.TableKey:
        return key.TableKey(
            collection="SETTLEMENTS",
            name="DAYTRACK",
            version=5
        )

    @staticmethod
    def from_row(row: List[str]) -> "DayTrack":
        return DayTrack(
            settlementdate=dt.datetime.strptime(row[4], "%Y/%m/%d %H:%M:%S").date(),
            expostrunno=decimal.Decimal(row[9]),
            lastchanged=dt.datetime.strptime(row[10], "%Y/%m/%d %H:%M:%S")
        )


@dataclass(frozen=True)
class NmasRecovery:
    settlementdate: dt.date
    versionno: decimal.Decimal
    periodid: decimal.Decimal
    participantid: str
    service: str
    contractid: str
    paymenttype: str
    regionid: str
    rbf: Optional[decimal.Decimal]
    payment_amount: Optional[decimal.Decimal]
    participant_energy: Optional[decimal.Decimal]
    region_energy: Optional[decimal.Decimal]
    recovery_amount: Optional[decimal.Decimal]
    lastchanged: Optional[dt.datetime]
    participant_generation: Optional[decimal.Decimal]
    region_generation: Optional[decimal.Decimal]
    recovery_amount_customer: Optional[decimal.Decimal]
    recovery_amount_generator: Optional[decimal.Decimal]

    @staticmethod
    def key() -> key.TableKey:
        return key.TableKey(
            collection="SETTLEMENTS",
            name="NMAS_RECOVERY",
            version=2
        )

    @staticmethod
    def from_row(row: List[str]) -> "NmasRecovery":
        return NmasRecovery(
            settlementdate=dt.datetime.strptime(row[4], "%Y/%m/%d %H:%M:%S").date(),
            versionno=decimal.Decimal(row[5]),
            periodid=decimal.Decimal(row[6]),
            participantid=row[7],
            service=row[8],
            contractid=row[9],
            paymenttype=row[10],
            regionid=row[11],
            rbf=opt_decimal(row[12]),
            payment_amount=opt_decimal(row[13]),
            participant_energy=opt_decimal(row[14]),
            region_energy=opt_decimal(row[15]),
            recovery_amount=opt_decimal(row[16]),
            lastchanged=dt.datetime.strptime(row[17], "%Y/%m/%d %H:%M:%S"),
            participant_generation=opt_decimal(row[18]),
            region_generation=opt_decimal(row[19]),
            recovery_amount_customer=opt_decimal(row[20]),
            recovery_amount_generator=opt_decimal(row[21]),
        )


@dataclass(frozen=True)
class Cpdata:
    settlementdate: dt.date
    versionno: decimal.Decimal
    periodid: decimal.Decimal
    participantid: str
    tcpid: str
    regionid: Optional[str]
    igenergy: Optional[decimal.Decimal]
    xgenergy: Optional[decimal.Decimal]
    inenergy: Optional[decimal.Decimal]
    xnenergy: Optional[decimal.Decimal]
    ipower: Optional[decimal.Decimal]
    xpower: Optional[decimal.Decimal]
    rrp: Optional[decimal.Decimal]
    eep: Optional[decimal.Decimal]
    tlf: Optional[decimal.Decimal]
    cprrp: Optional[decimal.Decimal]
    cpeep: Optional[decimal.Decimal]
    ta: Optional[decimal.Decimal]
    ep: Optional[decimal.Decimal]
    apc: Optional[decimal.Decimal]
    resc: Optional[decimal.Decimal]
    resp: Optional[decimal.Decimal]
    meterrunno: Optional[decimal.Decimal]
    hostdistributor: Optional[str]
    mda: str
    lastchanged: Optional[dt.datetime]
    meterdata_source: Optional[str]

    @staticmethod
    def key() -> key.TableKey:
        return key.TableKey(
            collection="SETTLEMENTS",
            name="CPDATA",
            version=5,
        )

    @staticmethod
    def from_row(row: List[str]) -> "Cpdata":
        return Cpdata(
            settlementdate=dt.datetime.strptime(row[4], "%Y/%m/%d %H:%M:%S").date(),
            versionno=decimal.Decimal(row[5]),
            periodid=decimal.Decimal(row[6]),
            participantid=row[7],
            tcpid=row[8],
            regionid=row[9],
            igenergy=opt_decimal(row[10]),
            xgenergy=opt_decimal(row[11]),
            inenergy=opt_decimal(row[12]),
            xnenergy=opt_decimal(row[13]),
            ipower=opt_decimal(row[14]),
            xpower=opt_decimal(row[15]),
            rrp=opt_decimal(row[16]),
            eep=opt_decimal(row[17]),
            tlf=opt_decimal(row[18]),
            cprrp=opt_decimal(row[19]),
            cpeep=opt_decimal(row[20]),
            ta=opt_decimal(row[21]),
            ep=opt_decimal(row[22]),
            apc=opt_decimal(row[23]),
            resc=opt_decimal(row[24]),
            resp=opt_decimal(row[25]),
            meterrunno=opt_decimal(row[26]),
            hostdistributor=row[27],
            mda=row[28],
            lastchanged=dt.datetime.strptime(row[29], "%Y/%m/%d %H:%M:%S"),
            meterdata_source=row[30],
        )


@dataclass(frozen=True)
class FcasRecovery:
    settlementdate: dt.date
    versionno: str
    participantid: str
    regionid: str
    periodid: decimal.Decimal
    lower6sec_recovery: Optional[decimal.Decimal]
    raise6sec_recovery: Optional[decimal.Decimal]
    lower60sec_recovery: Optional[decimal.Decimal]
    raise60sec_recovery: Optional[decimal.Decimal]
    lower5min_recovery: Optional[decimal.Decimal]
    raise5min_recovery: Optional[decimal.Decimal]
    lowerreg_recovery: Optional[decimal.Decimal]
    raisereg_recovery: Optional[decimal.Decimal]
    lastchanged: Optional[dt.datetime]
    lower6sec_recovery_gen: Optional[decimal.Decimal]
    raise6sec_recovery_gen: Optional[decimal.Decimal]
    lower60sec_recovery_gen: Optional[decimal.Decimal]
    raise60sec_recovery_gen: Optional[decimal.Decimal]
    lower5min_recovery_gen: Optional[decimal.Decimal]
    raise5min_recovery_gen: Optional[decimal.Decimal]
    lowerreg_recovery_gen: Optional[decimal.Decimal]
    raisereg_recovery_gen: Optional[decimal.Decimal]

    @staticmethod
    def key() -> key.TableKey:
        return key.TableKey(
            collection="SETTLEMENTS",
            name="FCAS_RECOVERY",
            version=6
        )

    @staticmethod
    def from_row(row: List[str]) -> "FcasRecovery":
        return FcasRecovery(
            settlementdate=dt.datetime.strptime(row[4], "%Y/%m/%d %H:%M:%S").date(),
            versionno=row[5],
            participantid=row[6],
            regionid=row[7],
            periodid=decimal.Decimal(row[8]),
            lower6sec_recovery=opt_decimal(row[9]),
            raise6sec_recovery=opt_decimal(row[10]),
            lower60sec_recovery=opt_decimal(row[11]),
            raise60sec_recovery=opt_decimal(row[12]),
            lower5min_recovery=opt_decimal(row[13]),
            raise5min_recovery=opt_decimal(row[14]),
            lowerreg_recovery=opt_decimal(row[15]),
            raisereg_recovery=opt_decimal(row[16]),
            lastchanged=dt.datetime.strptime(row[17], "%Y/%m/%d %H:%M:%S"),
            lower6sec_recovery_gen=opt_decimal(row[18]),
            raise6sec_recovery_gen=opt_decimal(row[19]),
            lower60sec_recovery_gen=opt_decimal(row[20]),
            raise60sec_recovery_gen=opt_decimal(row[21]),
            lower5min_recovery_gen=opt_decimal(row[22]),
            raise5min_recovery_gen=opt_decimal(row[23]),
            lowerreg_recovery_gen=opt_decimal(row[24]),
            raisereg_recovery_gen=opt_decimal(row[25]),
        )


@dataclass(frozen=True)
class Marketfees:
    settlementdate: dt.date
    runno: decimal.Decimal
    participantid: str
    periodid: decimal.Decimal
    marketfeeid: str
    marketfeevalue: Optional[decimal.Decimal]
    energy: Optional[decimal.Decimal]
    lastchanged: Optional[dt.datetime]
    participantcategoryid: str

    @staticmethod
    def key() -> key.TableKey:
        return key.TableKey(
            collection="SETTLEMENTS",
            name="MARKETFEES",
            version=5
        )

    @staticmethod
    def from_row(row: List[str]) -> "Marketfees":
        return Marketfees(
            settlementdate=dt.datetime.strptime(row[4], "%Y/%m/%d %H:%M:%S").date(),
            runno=decimal.Decimal(row[5]),
            participantid=row[6],
            periodid=decimal.Decimal(row[7]),
            marketfeeid=row[8],
            marketfeevalue=opt_decimal(row[9]),
            energy=opt_decimal(row[10]),
            lastchanged=dt.datetime.strptime(row[11], "%Y/%m/%d %H:%M:%S"),
            participantcategoryid=row[12],
        )


@dataclass(frozen=True)
class Reallocations:
    settlementdate: dt.date
    runno: decimal.Decimal
    periodid: decimal.Decimal
    participantid: str
    reallocationid: str
    reallocationvalue: Optional[decimal.Decimal]
    energy: Optional[decimal.Decimal]
    rrp: Optional[decimal.Decimal]
    lastchanged: Optional[dt.datetime]

    @staticmethod
    def key() -> key.TableKey:
        return key.TableKey(
            collection="SETTLEMENTS",
            name="REALLOCATIONS",
            version=5
        )

    @staticmethod
    def from_row(row: List[str]) -> "Reallocations":
        return Reallocations(
            settlementdate=dt.datetime.strptime(row[4], "%Y/%m/%d %H:%M:%S").date(),
            runno=decimal.Decimal(row[5]),
            periodid=decimal.Decimal(row[6]),
            participantid=row[7],
            reallocationid=row[8],
            reallocationvalue=opt_decimal(row[9]),
            energy=opt_decimal(row[10]),
            rrp=opt_decimal(row[11]),
            lastchanged=dt.datetime.strptime(row[12], "%Y/%m/%d %H:%M:%S"),
        )
