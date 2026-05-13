"""Тесты для CLI (точки входа)."""

from unittest.mock import patch

import pytest

from video_report.cli import main, parse_args


def test_parse_args(monkeypatch):
    """Проверка парсинга аргументов командной строки."""
    test_args = ["main.py", "--files", "a.csv", "b.csv", "--report", "clickbait"]
    monkeypatch.setattr("sys.argv", test_args)

    args = parse_args()
    assert args.files == ["a.csv", "b.csv"]
    assert args.report == "clickbait"


def test_main_success(sample_csv_file, capsys):
    """Проверка успешного выполнения main с реальным файлом."""
    with patch(
        "sys.argv", ["main.py", "--files", sample_csv_file, "--report", "clickbait"]
    ):
        main()

    captured = capsys.readouterr()
    assert "Кликбейт A" in captured.out
    assert "Кликбейт B" in captured.out
    assert "Хорошее видео" not in captured.out


def test_main_no_files(capsys):
    """Проверка обработки отсутствия файлов."""
    with patch(
        "sys.argv", ["main.py", "--files", "nonexistent.csv", "--report", "clickbait"]
    ):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 1

    captured = capsys.readouterr()
    assert "Файл не найден" in captured.err


def test_main_unknown_report(sample_csv_file, capsys):
    """Проверка обработки неизвестного отчёта."""
    with patch(
        "sys.argv", ["main.py", "--files", sample_csv_file, "--report", "unknown"]
    ):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 1

    captured = capsys.readouterr()
    assert "Неизвестный отчёт" in captured.err


def test_main_no_data(tmp_path, capsys):
    """Проверка обработки пустого CSV-файла."""
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("title,ctr,retention_rate\n")

    with patch(
        "sys.argv", ["main.py", "--files", str(empty_file), "--report", "clickbait"]
    ):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 1

    captured = capsys.readouterr()
    assert "В указанных файлах нет данных." in captured.err
