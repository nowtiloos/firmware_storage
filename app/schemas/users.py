from pydantic import BaseModel, EmailStr


class SUsers(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str
    access_to_read: bool
    access_to_write: bool
    tg_id: int

    class Config:
        from_attributes = True
