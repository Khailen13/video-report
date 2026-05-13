"""Фикстуры pytest для тестирования."""

import tempfile

import pytest


@pytest.fixture
def sample_csv_content():
    return """title,ctr,retention_rate,views,likes,avg_watch_time
Кликбейт A,22.5,28,128700,3150,3.1
Хорошее видео,9.5,82,31500,890,8.9
Кликбейт B,19.0,38,87600,2100,4.5
Пограничное,16.5,42,54100,1320,4.8
Неверное,invalid,50,100,5,1.0
"""


@pytest.fixture
def sample_csv_file(sample_csv_content):
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".csv", delete=False
    ) as f:
        f.write(sample_csv_content)
        return f.name


@pytest.fixture
def multiple_csv_files(sample_csv_content):
    files = []
    for _ in range(2):
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", suffix=".csv", delete=False
        ) as f:
            f.write(sample_csv_content)
            files.append(f.name)
    return files
