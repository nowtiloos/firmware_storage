from typing import Annotated
from enum import Enum

from fastapi import Query, UploadFile
from pydantic import BaseModel


class SFirmware(BaseModel):
    file_name: str
    truck_model: str
    engine_model: str
    ecu_model: str
    flasher: str
    file_path: str
    user_uploaded: str
    file_size: int

    class Config:
        from_attributes = True


class TruckEnum(str, Enum):
    mercedes = "Mercedes-Benz"
    volvo_trucks = "VOLVO Trucks"
    renault_trucks = "RENAULT Trucks"
    kamaz = "KAMAZ"
    scania = "Scania"
    daf = "DAF"


class UploadFirmwareDTO(BaseModel):
    file: UploadFile
    truck_model: TruckEnum
    engine_model: str
    ecu_model: str
    flasher: str


class FirmwareSearchDTO(BaseModel):
    truck_model: TruckEnum
    engine_model: Annotated[str | None, Query(default=None)]
    ecu_model: Annotated[str | None, Query(default=None)]

