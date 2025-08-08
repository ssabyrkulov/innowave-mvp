from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.common.database import get_db
from src.common.security import verify_password
from src.repositories.users import UsersRepo
from src.auth.schemas import Token, RegisterIn
from src.auth.utils import create_access_token

router = APIRouter()

@router.post("/register", response_model=Token)
def register(data: RegisterIn, db: Session = Depends(get_db)):
    repo = UsersRepo(db)
    if repo.get_by_email(data.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = repo.create(email=data.email, password=data.password, full_name=data.full_name)
    token = create_access_token(user.id)
    return Token(access_token=token)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    repo = UsersRepo(db)
    user = repo.get_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    token = create_access_token(user.id)
    return Token(access_token=token)
