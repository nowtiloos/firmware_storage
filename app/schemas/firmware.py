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


class FirmwareSearchDTO(BaseModel):
    truck_model: str
    ecu_model: str
    modified: bool

