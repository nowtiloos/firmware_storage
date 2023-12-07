from dataclasses import dataclass
from enum import Enum

from pydantic import BaseModel


class TruckEnum(str, Enum):
    mercedes = "Mercedes Truck"
    volvo = "Volvo Truck"
    man = "MAN"
    renault = "Renault Truck"
    kamaz = "KamAZ"
    iveco = "Iveco"


class EcuModelEnum(str, Enum):
    edc7uc31 = "EDC7 UC31"
    edc7c3 = "EDC7 C3"
    edc17cp54 = "EDC17 CP54"


class SFlash(BaseModel):
    truck_model: str
    engine_model: str
    ecu_model: str
    firmware: str
    flasher: str
    modified: bool
    file_name: str
    file_path: None

    class Config:
        from_attributes = True


@dataclass
class FlashSearch:
    truck_model: TruckEnum
    ecu_model: EcuModelEnum
    modified: bool
