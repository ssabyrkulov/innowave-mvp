from pydantic import BaseModel
import os
from datetime import timedelta

class Settings(BaseModel):
    # ❶ Если есть готовый URL — используем его
    DATABASE_URL_ENV: str | None = os.getenv("DATABASE_URL")

    # ❷ Иначе собираем из кусков (на локалке/docker-compose)
    DB_USER: str = os.getenv("POSTGRES_USER", "admin")
    DB_PASS: str = os.getenv("POSTGRES_PASSWORD", "admin")
    DB_NAME: str = os.getenv("POSTGRES_DB", "inh_mvp")
    DB_HOST: str = os.getenv("POSTGRES_HOST", "db")
    DB_PORT: str = os.getenv("POSTGRES_PORT", "5432")

    JWT_SECRET: str = os.getenv("JWT_SECRET", "supersecretkey")
    JWT_ALG: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_MIN: int = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

    @property
    def DATABASE_URL(self) -> str:
        if self.DATABASE_URL_ENV:
            return self.DATABASE_URL_ENV  # например: postgres://user:pass@host:5432/db?sslmode=require
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def ACCESS_EXPIRES(self) -> timedelta:
        return timedelta(minutes=self.JWT_ACCESS_MIN)

settings = Settings()
