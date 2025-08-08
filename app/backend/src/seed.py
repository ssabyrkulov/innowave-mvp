from sqlalchemy.orm import Session
from src.common.database import SessionLocal, Base, engine
from src.repositories.users import UsersRepo
from src.repositories.companies import CompaniesRepo

def seed():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    try:
        ur = UsersRepo(db)
        if not ur.get_by_email("admin@example.com"):
            ur.create(email="admin@example.com", password="admin123", full_name="Admin")
        cr = CompaniesRepo(db)
        if not cr.list(limit=1):
            cr.create({"name": "Innowave Hygiene", "inn": "123456789", "country": "KG"})
    finally:
        db.close()

if __name__ == "__main__":
    seed()
