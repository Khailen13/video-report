"""Фабрика отчётов: регистрация и получение экземпляров отчётов."""

from typing import Dict

from .base import BaseReport
from .clickbait import ClickbaitReport

_REPORTS: Dict[str, BaseReport] = {
    ClickbaitReport().name: ClickbaitReport(),
}


def get_report(name: str) -> BaseReport:
    """Вернуть экземпляр отчёта по имени."""
    if name not in _REPORTS:
        raise ValueError(
            f"Неизвестный отчёт: {name}. Доступны: {list(_REPORTS.keys())}"
        )
    return _REPORTS[name]


def list_reports() -> list:
    """Вернуть список имён доступных отчётов."""
    return list(_REPORTS.keys())
