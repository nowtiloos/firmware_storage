from pydantic import BaseModel


class SFirmwareCalibrators(BaseModel):
    name: str
    phone_number: int

    class Config:
        from_attributes = True
