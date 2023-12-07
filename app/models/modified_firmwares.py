from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Users(Base):
    __tablename__ = "modified_firmwares"

    file_name: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    file_name_original: Mapped[str] = mapped_column(nullable=False)
    calibrator_name: Mapped[str] = mapped_column(nullable=False)
    file_path: Mapped[str]
    user_uploaded: Mapped[str] = mapped_column(nullable=False)

    def __str__(self) -> str:
        return f"Firmware: {self.file_path}"
