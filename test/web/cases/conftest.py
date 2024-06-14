#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 我的饭
@file: conftest.py
@time: 2024/6/14 19:19
"""
import pytest

from test.web.cases import home_page


@pytest.fixture(scope='package', autouse=True)
def quit_driver():
    yield
    home_page.quit()

