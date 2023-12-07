from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Users(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    access_to_read: Mapped[bool] = mapped_column(nullable=False, default=False)
    access_to_write: Mapped[bool] = mapped_column(nullable=False, default=False)
    tg_id: Mapped[int]

    def __str__(self) -> str:
        return f"Пользователь: {self.name}"
