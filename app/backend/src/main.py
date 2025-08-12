from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# API routers
from src.api.v1 import health, companies, reports
from src.auth import routes as auth_routes


app = FastAPI(
    title="Innowave MVP API",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

# CORS (добавишь адрес фронтенда, когда поднимем его на Render)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: сузить до URL фронта, например "https://innowave-frontend.onrender.com"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root (просто чтобы / не отдавал 404)
@app.get("/", tags=["Health"])
def root():
    return {"service": "innowave-mvp", "status": "ok"}

# Routers
app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])
app.include_router(auth_routes.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(companies.router, prefix="/api/v1/companies", tags=["Companies"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["Reports"])
