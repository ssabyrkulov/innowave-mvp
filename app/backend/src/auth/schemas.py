from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginIn(BaseModel):
    username: EmailStr
    password: str

class RegisterIn(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None
