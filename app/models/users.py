from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Users(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]
    access_to_read: Mapped[bool] = mapped_column(default=False)
    access_to_write: Mapped[bool] = mapped_column(default=False)
    tg_id: Mapped[int]

    def __str__(self) -> str:
        return f"Пользователь: {self.name}"
