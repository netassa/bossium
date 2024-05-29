# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: test_home_page.py
@time: 2024/5/29 14:31
"""
from test.web.pages.home_page import HomePage
from test.web.pages import base_page


class TestHomePage:

    def test_home(self):
        home_page = HomePage(base_page)
        assert '「深圳招聘网」海量深圳人才招聘信息' in home_page.title
