#!/usr/bin/env python3
# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: conftest.py
@time: 2024/6/12 0:22
"""
from datetime import datetime

import poium
import pytest
import selenium


def pytest_html_report_title(report):
    report.title = '自动化测试报告'


def format_timedelta_hms(td):
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f'{hours:02}:{minutes:02}:{seconds:02}'


def pytest_html_results_summary(prefix, session):
    prefix.extend([f"<p>Pytest invoked from {session.startpath}</p>"])


def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")
    cells.insert(1, f'<td class="col-time">{datetime.strftime(datetime.fromtimestamp(report.start), '%x %X')}</td>')
    cells.pop()


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata['Packages']['selenium'] = selenium.__version__
    metadata['Packages']['poium'] = poium.__version__


def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    cells.insert(1, '<th class="sortable time" data-column-type="time">StartTime</th>')
    cells.pop()
