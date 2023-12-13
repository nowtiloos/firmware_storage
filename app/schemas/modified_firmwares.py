from pydantic import BaseModel


class SModifiedFirmwares(BaseModel):
    file_name: str
    file_name_original: str
    calibrator_name: str
    file_path: str
    user_uploaded: str

    class Config:
        from_attributes = True
