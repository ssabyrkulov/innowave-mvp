from sqlalchemy.orm import Session
from datetime import date, datetime
from typing import List, Dict

from src.repositories.companies import Company
from src.repositories.companies import CompaniesRepo

def get_cfs(period: str, currency: str, db: Session) -> Dict:
    """
    Возвращает упрощённый отчёт ДДС: сумма входящих и исходящих по статьям за месяц
    """
    # TODO: Реализовать реальный запрос
    return {
        "period": period,
        "currency": currency,
        "inflows": [],
        "outflows": [],
        "net": 0
    }

def get_pnl(period: str, currency: str, db: Session) -> Dict:
    """
    Упрощённый P&L: Выручка - Себестоимость - Расходы
    """
    return {
        "period": period,
        "currency": currency,
        "revenue": 0,
        "cogs": 0,
        "expenses": 0,
        "profit": 0
    }

def get_balance(date_at: date, currency: str, db: Session) -> Dict:
    """
    Лёгкий баланс: остатки по счетам, дебиторка, кредиторка
    """
    return {
        "date": date_at,
        "currency": currency,
        "cash": 0,
        "accounts_receivable": 0,
        "accounts_payable": 0,
        "equity": 0
    }

def get_runway(currency: str, db: Session) -> Dict:
    """
    Runway: сколько дней хватит денег при текущем burn rate
    """
    return {
        "currency": currency,
        "runway_days": None,
        "burn_rate": 0
    }

def get_aging(report_type: str, db: Session) -> Dict:
    """
    Aging: разбивка задолженности по срокам
    """
    return {
        "type": report_type,
        "buckets": {
            "0-30": 0,
            "31-60": 0,
            "61-90": 0,
            "90+": 0
        }
    }
