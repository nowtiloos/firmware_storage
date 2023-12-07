from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from app.database.database import Base


class ModifiedFirmwares(Base):
    __tablename__ = "modified_firmwares"

    file_name: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    file_name_original: Mapped[str] = mapped_column(ForeignKey("firmwares.file_name"), nullable=False)
    calibrator_name: Mapped[str] = mapped_column(ForeignKey("firmware_calibrators.name"), nullable=False)
    file_path: Mapped[str]
    user_uploaded: Mapped[str] = mapped_column(ForeignKey("users.name"), nullable=False)

    def __str__(self) -> str:
        return f"Firmware: {self.file_path}"
