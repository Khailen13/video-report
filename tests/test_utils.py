"""Тесты для утилит чтения CSV."""

import pytest

from video_report.utils import read_csv_files


def test_read_csv_files_single(sample_csv_file):
    data = read_csv_files([sample_csv_file])
    assert len(data) == 5
    assert data[0]["title"] == "Кликбейт A"
    assert data[0]["ctr"] == "22.5"


def test_read_csv_files_multiple(multiple_csv_files):
    data = read_csv_files(multiple_csv_files)
    assert len(data) == 10


def test_read_csv_files_missing():
    with pytest.raises(FileNotFoundError):
        read_csv_files(["не_существует.csv"])


def test_read_csv_files_empty(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("title,ctr,retention_rate\n")
    data = read_csv_files([str(empty_file)])
    assert data == []
