from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from typing import Literal

from src.common.database import get_db
from src.services.reports import (
    get_cfs,
    get_pnl,
    get_balance,
    get_runway,
    get_aging,
)

router = APIRouter()

@router.get("/cfs")
def cash_flow_statement(
    period: str = Query(..., description="YYYY-MM"),
    currency: str = Query(..., description="Напр. KGS|USD|CNY"),
    db: Session = Depends(get_db),
):
    return get_cfs(period=period, currency=currency, db=db)

@router.get("/pnl")
def profit_and_loss(
    period: str = Query(..., description="YYYY-MM"),
    currency: str = Query(..., description="Напр. KGS|USD|CNY"),
    db: Session = Depends(get_db),
):
    return get_pnl(period=period, currency=currency, db=db)

@router.get("/balance")
def balance_report(
    date_at: date = Query(..., description="YYYY-MM-DD"),
    currency: str = Query(..., description="Напр. KGS|USD|CNY"),
    db: Session = Depends(get_db),
):
    return get_balance(date_at=date_at, currency=currency, db=db)

@router.get("/runway")
def runway_report(
    currency: str = Query(..., description="Напр. KGS|USD|CNY"),
    db: Session = Depends(get_db),
):
    return get_runway(currency=currency, db=db)

@router.get("/aging")
def aging_report(
    type: Literal["ar", "ap"] = Query(..., description="'ar' — дебиторка, 'ap' — кредиторка"),
    db: Session = Depends(get_db),
):
    return get_aging(report_type=type, db=db)
