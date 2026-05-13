"""Вспомогательные функции для чтения CSV-файлов."""

import csv
from pathlib import Path
from typing import Any, Dict, List


def read_csv_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    """Прочитать один или несколько CSV-файлов и объединить строки в список словарей."""
    all_rows = []
    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        with open(path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_rows.append(row)
    return all_rows
