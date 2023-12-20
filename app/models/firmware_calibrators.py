from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class FirmwareCalibrators(Base):
    __tablename__ = "firmware_calibrators"

    name: Mapped[str] = mapped_column(primary_key=True)
    phone_number: Mapped[int]

    def __str__(self) -> str:
        return f"Калибровщик: {self.name}"
