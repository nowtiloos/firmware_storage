from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Firmwares(Base):
    __tablename__ = "firmwares"

    file_name: Mapped[str] = mapped_column(primary_key=True)
    truck_model: Mapped[str]
    engine_model: Mapped[str]
    ecu_model: Mapped[str]
    flasher: Mapped[str]
    file_path: Mapped[str]
    file_size: Mapped[int]
    user_uploaded: Mapped[str] = mapped_column(ForeignKey("users.name"))

    def __repr__(self) -> str:
        return f"Firmware: {self.file_name}"
