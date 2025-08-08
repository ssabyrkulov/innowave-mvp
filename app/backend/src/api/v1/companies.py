from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.common.database import get_db
from src.common.deps import get_current_user
from src.schemas.companies import CompanyCreate, CompanyUpdate, CompanyOut
from src.repositories.companies import CompaniesRepo

router = APIRouter()

@router.get("/", response_model=List[CompanyOut])
def list_companies(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return CompaniesRepo(db).list()

@router.post("/", response_model=CompanyOut)
def create_company(payload: CompanyCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return CompaniesRepo(db).create(payload.dict())

@router.get("/{company_id}", response_model=CompanyOut)
def get_company(company_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    obj = CompaniesRepo(db).get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.put("/{company_id}", response_model=CompanyOut)
def update_company(company_id: int, payload: CompanyUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    repo = CompaniesRepo(db)
    obj = repo.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return repo.update(obj, payload.dict())

@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    repo = CompaniesRepo(db)
    obj = repo.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    repo.delete(obj)
    return {"status": "deleted"}
