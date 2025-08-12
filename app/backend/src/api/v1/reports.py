from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from typing import Optional

from src.common.database import get_db

router = APIRouter()

@router.get("/cfs")
def cash_flow_statement(
    period: str = Query(..., description="YYYY-MM"),
    currency: str = Query(...),
    db: Session = Depends(get_db)
):
    # TODO: Реализовать группировки по статьям и direction
    return {"period": period, "currency": currency, "data": []}

@router.get("/pnl")
def profit_and_loss(
    period: str = Query(..., description="YYYY-MM"),
    currency: str = Query(...),
    db: Session = Depends(get_db)
):
    # TODO: Выручка - Себестоимость - Расходы
    return {"period": period, "currency": currency, "data": []}

@router.get("/balance")
def balance_report(
    date_at: date = Query(...),
    currency: str = Query(...),
    db: Session = Depends(get_db)
):
    # TODO: Остатки по счетам + ДЗ - КЗ
    return {"date": date_at, "currency": currency, "data": []}

@router.get("/runway")
def runway_report(
    currency: str = Query(...),
    db: Session = Depends(get_db)
):
    # TODO: Остаток / Средний расход в день
    return {"currency": currency, "runway_days": None}

@router.get("/aging")
def aging_report(
    type: str = Query(..., description="'ar' или 'ap'"),
    db: Session = Depends(get_db)
):
    # TODO: Разбивка по срокам просрочки
    return {"type": type, "buckets": []}
