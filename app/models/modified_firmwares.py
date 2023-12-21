from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from app.database.database import Base


class ModifiedFirmwares(Base):
    __tablename__ = "modified_firmwares"

    file_name: Mapped[str] = mapped_column(primary_key=True)
    file_name_original: Mapped[str] = mapped_column(ForeignKey("firmwares.file_name"))
    calibrator_name: Mapped[str] = mapped_column(ForeignKey("firmware_calibrators.name"))
    file_path: Mapped[str]
    user_uploaded: Mapped[str] = mapped_column(ForeignKey("users.name"))

    def __str__(self) -> str:
        return f"Modified Firmware: {self.file_name}"
