from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Users(Base):
    __tablename__ = "firmware_calibrators"

    name: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    phone_number: Mapped[int] = mapped_column(nullable=False)

    def __str__(self) -> str:
        return f"Калибровщик: {self.name}"