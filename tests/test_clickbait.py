"""Тесты для логики отчёта clickbait."""

import pytest

from video_report.reports.clickbait import ClickbaitReport


@pytest.fixture
def report():
    return ClickbaitReport()


def test_clickbait_process(report):
    data = [
        {"title": "A", "ctr": "22.5", "retention_rate": "28"},
        {"title": "B", "ctr": "9.5", "retention_rate": "82"},
        {"title": "C", "ctr": "19.0", "retention_rate": "38"},
        {"title": "D", "ctr": "16.5", "retention_rate": "42"},
    ]
    result = report.process(data)
    assert len(result) == 2
    assert result[0]["title"] == "A"
    assert result[1]["title"] == "C"
    assert result[0]["ctr"] == 22.5
    assert result[0]["retention_rate"] == 28


def test_clickbait_boundaries(report):
    data = [
        {"title": "Низкий", "ctr": "15.0", "retention_rate": "39"},
        {"title": "Высокий", "ctr": "15.1", "retention_rate": "40"},
        {"title": "Валидный", "ctr": "20", "retention_rate": "35"},
    ]
    result = report.process(data)
    assert len(result) == 1
    assert result[0]["title"] == "Валидный"


def test_clickbait_invalid_numbers(report):
    data = [
        {"title": "Валидный", "ctr": "18", "retention_rate": "30"},
        {"title": "Плохой CTR", "ctr": "не число", "retention_rate": "25"},
        {"title": "Плохое удержание", "ctr": "20", "retention_rate": "abc"},
    ]
    result = report.process(data)
    assert len(result) == 1
    assert result[0]["title"] == "Валидный"


def test_clickbait_sorting(report):
    data = [
        {"title": "Низкий", "ctr": "18", "retention_rate": "30"},
        {"title": "Высокий", "ctr": "25", "retention_rate": "35"},
        {"title": "Средний", "ctr": "20", "retention_rate": "28"},
    ]
    result = report.process(data)
    titles = [r["title"] for r in result]
    assert titles == ["Высокий", "Средний", "Низкий"]


def test_get_report_unknown():
    """Проверка, что при запросе неизвестного отчёта возникает ошибка."""
    from video_report.reports import get_report

    with pytest.raises(ValueError, match="Неизвестный отчёт: unknown"):
        get_report("unknown")


def test_list_reports():
    """Проверка, что list_reports возвращает ожидаемые имена."""
    from video_report.reports import list_reports

    reports = list_reports()
    assert "clickbait" in reports
    assert isinstance(reports, list)
