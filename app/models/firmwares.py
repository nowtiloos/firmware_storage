from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Firmwares(Base):
    __tablename__ = "firmwares"

    file_name: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    truck_model: Mapped[str] = mapped_column(nullable=False)
    engine_model: Mapped[str] = mapped_column(nullable=False)
    ecu_model: Mapped[str] = mapped_column(nullable=False)
    firmware: Mapped[str] = mapped_column(nullable=False)
    flasher: Mapped[str] = mapped_column(nullable=False)
    file_path: Mapped[str]
    user_uploaded: Mapped[str] = mapped_column(ForeignKey("users.name"), nullable=False)

    def __str__(self) -> str:
        return f"Firmware: {self.file_path}"
