"""Отчёт «кликбейт»: высокий CTR (>15) и низкое удержание (<40)."""

from typing import Any, Dict, List

from .base import BaseReport


class ClickbaitReport(BaseReport):
    """Отчёт для выявления кликбейтных видео."""

    @property
    def name(self) -> str:
        return "clickbait"

    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Отфильтровать, отсортировать и выбрать нужные колонки."""
        filtered = self._filter(data)
        sorted_data = self._sort(filtered)
        return self._select_columns(sorted_data)

    def _filter(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Оставить строки с ctr > 15 и retention_rate < 40, пропуская нечисловые."""
        result = []
        for row in data:
            try:
                ctr = float(row.get("ctr", 0))
                retention = float(row.get("retention_rate", 100))
                if ctr > 15 and retention < 40:
                    result.append(row)
            except (ValueError, TypeError):
                continue
        return result

    def _sort(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Сортировка по убыванию CTR."""
        return sorted(data, key=lambda x: float(x["ctr"]), reverse=True)

    def _select_columns(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Оставить только title, ctr и retention_rate, преобразовав в числа."""
        return [
            {
                "title": row["title"],
                "ctr": float(row["ctr"]),
                "retention_rate": float(row["retention_rate"]),
            }
            for row in data
        ]
