# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: common_component_page.py.py
@time: 2024/6/9 23:16
"""
from poium import Element

from test.web.pages.base_page import BasePage


class HeaderPage(BasePage):
    login_button = Element('.header-login-btn')

    def login_or_sign_in(self):
        self.login_button.click()


class FooterPage(BasePage):
    pass
