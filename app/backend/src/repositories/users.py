from sqlalchemy.orm import Session
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.common.database import Base
from src.common.security import hash_password

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

class UsersRepo:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, password: str, full_name: str | None = None):
        u = User(email=email, password_hash=hash_password(password), full_name=full_name, is_active=True)
        self.db.add(u)
        self.db.commit()
        self.db.refresh(u)
        return u

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_by_id(self, user_id: int):
        return self.db.get(User, user_id)
