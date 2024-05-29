# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: test_login_page.py
@time: 2024/5/28 20:12
"""
from test.web.pages import base_page
from test.web.pages.login_page import LoginPage


class TestLoginPage:

    def test_login(self):
        login_page = LoginPage(base_page)
        login_page.login()
        assert login_page.toast.text == "请先完成验证"

