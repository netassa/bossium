# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: home_page.py
@time: 2024/5/28 19:49
"""
from poium import Element

from test.web.pages.base_page import BasePage
from . import login_page


class HomePage(BasePage):
    login_button = Element('.header-login-btn')

    def __init__(self, base: BasePage = None):
        self.driver = base.driver
        # login_page.login()   # 如果可登录的话，每一个页面都要先登录
