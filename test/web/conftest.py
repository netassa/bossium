#!/usr/bin/env python3
# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: conftest.py
@time: 2024/6/12 0:22
"""
import pytest
import pytest_html

from . import home_page


@pytest.fixture(scope='session', autouse=True)
def quit_driver():
    yield
    home_page.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call" and report.failed:
        extras.append(pytest_html.extras.image(home_page.get_screenshot_as_base64(), mime_type='image/png'))
        report.extras = extras
    report.description = str(item.function.__doc__)

