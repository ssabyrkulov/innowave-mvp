from fastapi import FastAPI
from src.api.v1 import health, companies
from src.auth import routes as auth_routes

app = FastAPI(title="Innowave MVP API", version="1.0.0")

# Health check
app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])
# Auth
app.include_router(auth_routes.router, prefix="/api/v1/auth", tags=["Auth"])
# Companies CRUD
app.include_router(companies.router, prefix="/api/v1/companies", tags=["Companies"])
