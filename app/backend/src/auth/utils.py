from datetime import datetime
from src.config import settings
from jose import jwt

def create_access_token(sub: int) -> str:
    expire = datetime.utcnow() + settings.ACCESS_EXPIRES
    to_encode = {"sub": str(sub), "exp": expire}
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALG)
