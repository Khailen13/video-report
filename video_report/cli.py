"""Точка входа CLI: разбор аргументов, загрузка данных, запуск отчёта, вывод таблицы."""

import argparse
import sys

from tabulate import tabulate

from video_report.reports import get_report, list_reports
from video_report.utils import read_csv_files


def parse_args():
    parser = argparse.ArgumentParser(
        description="Генерация отчётов по метрикам видео с YouTube из CSV-файлов."
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Пути к CSV-файлам (один или несколько).",
    )
    parser.add_argument(
        "--report", required=True, help=f"Имя отчёта. Доступны: {list_reports()}"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        data = read_csv_files(args.files)
        if not data:
            print("В указанных файлах нет данных.", file=sys.stderr)
            sys.exit(1)

        report = get_report(args.report)
        result = report.process(data)

        if result:
            print(tabulate(result, headers="keys", tablefmt="grid"))
        else:
            print("Нет записей, соответствующих условиям отчёта.")

    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
