from typing import List, Optional
import dateutil.parser as du
import datetime as dt
import aemo.key as key

from pydantic.dataclasses import dataclass
from pydantic import constr
import decimal

# can throw ValueError due to date parsing


@dataclass(frozen=True)
class DayTrack:
    settlementdate: dt.date
    expostrunno: decimal.Decimal
    lastchanged: dt.datetime

    @staticmethod
    def key() -> key.TableKey:
        raise Exception("TODO")

    @staticmethod
    def from_row(row: List[str]) -> "DayTrack":
        return DayTrack(
            settlementdate=du.parse(row[4], dayfirst=True).date(),
            expostrunno=row[9],
            lastchanged=du.parse(row[10], dayfirst=True),
        )


@dataclass(frozen=True)
class NmasRecovery:
    settlementdate: dt.date
    versionno: decimal.Decimal
    periodid: decimal.Decimal
    participantid: constr(max_length=20)
    service: constr(max_length=10)
    contractid: constr(max_length=10)
    paymenttype: constr(max_length=20)
    regionid: constr(max_length=10)
    rbf: decimal.Decimal
    payment_amount: decimal.Decimal
    participant_energy: decimal.Decimal
    region_energy: decimal.Decimal
    recovery_amount: decimal.Decimal
    lastchanged: dt.datetime
    participant_generation: decimal.Decimal
    region_generation: decimal.Decimal
    recovery_amount_customer: decimal.Decimal
    recovery_amount_generator: decimal.Decimal

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
            settlementdate=du.parse(row[4], dayfirst=True).date(),
            versionno=row[5],
            periodid=row[6],
            participantid=row[7],
            service=row[8],
            contractid=row[9],
            paymenttype=row[10],
            regionid=row[11],
            rbf=row[12],
            payment_amount=row[13],
            participant_energy=row[14],
            region_energy=row[15],
            recovery_amount=row[16],
            lastchanged=du.parse(row[17], dayfirst=True),
            participant_generation=row[18],
            region_generation=row[19],
            recovery_amount_customer=row[20],
            recovery_amount_generator=row[21],
        )


@dataclass(frozen=True)
class Cpdata:
    settlementdate: dt.date
    versionno: decimal.Decimal
    periodid: decimal.Decimal
    participantid: constr(max_length=10)
    tcpid: constr(max_length=10)
    regionid: constr(max_length=10)
    igenergy: decimal.Decimal
    xgenergy: decimal.Decimal
    inenergy: decimal.Decimal
    xnenergy: decimal.Decimal
    ipower: decimal.Decimal
    xpower: decimal.Decimal
    rrp: decimal.Decimal
    eep: decimal.Decimal
    tlf: decimal.Decimal
    cprrp: decimal.Decimal
    cpeep: decimal.Decimal
    ta: decimal.Decimal
    ep: decimal.Decimal
    apc: str  # field is no longer used
    resc: str  # field is no longer used
    resp: str  # field is no longer used 
    meterrunno: decimal.Decimal
    hostdistributor: constr(max_length=10)
    mda: constr(max_length=10)
    lastchanged: dt.datetime
    meterdata_source: constr(max_length=10)

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
            settlementdate=du.parse(row[4], dayfirst=True).date(),
            versionno=row[5],
            periodid=row[6],
            participantid=row[7],
            tcpid=row[8],
            regionid=row[9],
            igenergy=row[10],
            xgenergy=row[11],
            inenergy=row[12],
            xnenergy=row[13],
            ipower=row[14],
            xpower=row[15],
            rrp=row[16],
            eep=row[17],
            tlf=row[18],
            cprrp=row[19],
            cpeep=row[20],
            ta=row[21],
            ep=row[22],
            apc=row[23],
            resc=row[24],
            resp=row[25],
            meterrunno=row[26],
            hostdistributor=row[27],
            mda=row[28],
            lastchanged=du.parse(row[29], dayfirst=True),
            meterdata_source=row[30],
        )


@dataclass(frozen=True)
class FcasRecovery:
    settlementdate: dt.date
    versionno: constr(max_length=3)
    participantid: constr(max_length=10)
    regionid: constr(max_length=10)
    periodid: decimal.Decimal
    lower6sec_recovery: decimal.Decimal
    raise6sec_recovery: decimal.Decimal
    lower60sec_recovery: decimal.Decimal
    raise60sec_recovery: decimal.Decimal
    lower5min_recovery: decimal.Decimal
    raise5min_recovery: decimal.Decimal
    lowerreg_recovery: decimal.Decimal
    raisereg_recovery: decimal.Decimal
    lastchanged: dt.datetime
    lower6sec_recovery_gen: decimal.Decimal
    raise6sec_recovery_gen: decimal.Decimal
    lower60sec_recovery_gen: decimal.Decimal
    raise60sec_recovery_gen: decimal.Decimal
    lower5min_recovery_gen: decimal.Decimal
    raise5min_recovery_gen: decimal.Decimal
    lowerreg_recovery_gen: decimal.Decimal
    raisereg_recovery_gen: decimal.Decimal

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
            settlementdate=du.parse(row[4], dayfirst=True).date(),
            versionno=row[5],
            participantid=row[6],
            regionid=row[7],
            periodid=row[8],
            lower6sec_recovery=row[9],
            raise6sec_recovery=row[10],
            lower60sec_recovery=row[11],
            raise60sec_recovery=row[12],
            lower5min_recovery=row[13],
            raise5min_recovery=row[14],
            lowerreg_recovery=row[15],
            raisereg_recovery=row[16],
            lastchanged=du.parse(row[17], dayfirst=True),
            lower6sec_recovery_gen=row[18],
            raise6sec_recovery_gen=row[19],
            lower60sec_recovery_gen=row[20],
            raise60sec_recovery_gen=row[21],
            lower5min_recovery_gen=row[22],
            raise5min_recovery_gen=row[23],
            lowerreg_recovery_gen=row[24],
            raisereg_recovery_gen=row[25],
        )


@dataclass(frozen=True)
class Marketfees:
    settlementdate: dt.date
    runno: decimal.Decimal
    participantid: constr(max_length=10)
    periodid: decimal.Decimal
    marketfeeid: constr(max_length=10)
    marketfeevalue: decimal.Decimal
    energy: decimal.Decimal
    lastchanged: dt.datetime
    participantcategoryid: constr(max_length=10)

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
            settlementdate=du.parse(row[4], dayfirst=True).date(),
            runno=row[5],
            participantid=row[6],
            periodid=row[7],
            marketfeeid=row[8],
            marketfeevalue=row[9],
            energy=row[10],
            lastchanged=du.parse(row[11], dayfirst=True),
            participantcategoryid=row[12],
        )
