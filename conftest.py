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
import pytest_html
import selenium


def pytest_html_report_title(report):
    report.title = '自动化测试报告'


def pytest_html_results_summary(prefix, session):
    prefix.extend([f"<p>Pytest invoked from {session.startpath}</p>"])


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras
    report.description = str(item.function.__doc__)


def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')


def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")
    cells.insert(1, f'<td class="col-time">{datetime.now()}</td>')


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata['Packages']['selenium'] = selenium.__version__
    metadata['Packages']['poium'] = poium.__version__
