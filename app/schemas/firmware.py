from pydantic import BaseModel


class SFirmware(BaseModel):
    file_name: str
    truck_model: str
    engine_model: str
    ecu_model: str
    firmware: str
    flasher: str
    file_path: str
    user_uploaded: str

    class Config:
        from_attributes = True


class SFirmwareSearch(BaseModel):
    truck_model: str
    ecu_model: str
    modified: bool


class SNewFirmware(BaseModel):
    file_name: str
    truck_model: str
    engine_model: str
    ecu_model: str
    firmware: str
    flasher: str
    user_uploaded: str
