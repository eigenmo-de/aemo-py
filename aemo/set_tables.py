from typing import List, Any, Callable
from dataclasses import dataclass
import dateutil.parser as du
import datetime as dt
import aemo.key as key

# can throw ValueError due to date parsing


@dataclass(frozen=True)
class DayTrack:
    settlementdate: dt.date
    expostrunno: str
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
class NmasRecovery2:
    settlementdate: dt.date
    versionno: str
    periodid: str
    participantid: str
    service: str
    contractid: str
    paymenttype: str
    regionid: str
    rbf: str
    payment_amount: str
    participant_energy: str
    region_energy: str
    recovery_amount: str
    lastchanged: dt.datetime
    participant_generation: str
    region_generation: str
    recovery_amount_customer: str
    recovery_amount_generator: str

    @staticmethod
    def key() -> key.TableKey:
        return key.TableKey(
            collection="SETTLEMENTS",
            name="NMAS_RECOVERY",
            version=2
        )

    @staticmethod
    def from_row(row: List[str]) -> "NmasRecovery2":
        return NmasRecovery2(
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
class Cpdata5:
    settlementdate: dt.date
    versionno: str
    periodid: str
    participantid: str
    tcpid: str
    regionid: str
    igenergy: str
    xgenergy: str
    inenergy: str
    xnenergy: str
    ipower: str
    xpower: str
    rrp: str
    eep: str
    tlf: str
    cprrp: str
    cpeep: str
    ta: str
    ep: str
    apc: str
    resc: str
    resp: str
    meterrunno: str
    hostdistributor: str
    mda: str
    lastchanged: dt.datetime
    meterdata_source: str

    @staticmethod
    def key() -> key.TableKey:
        return key.TableKey(
            collection="SETTLEMENTS",
            name="CPDATA",
            version=5,
        )

    @staticmethod
    def from_row(row: List[str]) -> "Cpdata5":
        return Cpdata5(
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
class FcasRecovery6:
    settlementdate: dt.date
    versionno: str
    participantid: str
    regionid: str
    periodid: str
    lower6sec_recovery: str
    raise6sec_recovery: str
    lower60sec_recovery: str
    raise60sec_recovery: str
    lower5min_recovery: str
    raise5min_recovery: str
    lowerreg_recovery: str
    raisereg_recovery: str
    lastchanged: dt.datetime
    lower6sec_recovery_gen: str
    raise6sec_recovery_gen: str
    lower60sec_recovery_gen: str
    raise60sec_recovery_gen: str
    lower5min_recovery_gen: str
    raise5min_recovery_gen: str
    lowerreg_recovery_gen: str
    raisereg_recovery_gen: str

    @staticmethod
    def key() -> key.TableKey:
        return key.TableKey(
            collection="SETTLEMENTS",
            name="FCAS_RECOVERY",
            version=6
        )

    @staticmethod
    def from_row(row: List[str]) -> "FcasRecovery6":
        return FcasRecovery6(
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
class Marketfees5:
    settlementdate: dt.date
    runno: str
    participantid: str
    periodid: str
    marketfeeid: str
    marketfeevalue: str
    energy: str
    lastchanged: dt.datetime
    participantcategoryid: str

    @staticmethod
    def key() -> key.TableKey:
        return key.TableKey(
            collection="SETTLEMENTS",
            name="MARKETFEES",
            version=5
        )

    @staticmethod
    def from_row(row: List[str]) -> "Marketfees5":
        return Marketfees5(
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


def mapping(key: key.TableKey) -> Callable[[List[str]], Any]:
    to_fn = {
        Cpdata5.key():
        Cpdata5.from_row,
        FcasRecovery6.key():
        FcasRecovery6.from_row,
        Marketfees5.key():
        Marketfees5.from_row,
        NmasRecovery2.key():
        NmasRecovery2.from_row,
    }
    return to_fn[key]
