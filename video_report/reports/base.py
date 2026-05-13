"""Базовые классы для отчётов."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseReport(ABC):
    """Абстрактный отчёт: каждый новый отчёт должен реализовать name и process."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Уникальное имя отчёта (совпадает с аргументом --report)."""
        pass

    @abstractmethod
    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Обработать сырые данные из CSV и вернуть строки финального отчёта."""
        pass
