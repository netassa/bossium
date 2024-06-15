# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: test_02_home_page.py
@time: 2024/5/29 14:31
"""
from test.web import home_page


class TestHomePage:

    def test_home(self):
        """测试主页"""
        home_page.go_to_my_page()
        assert '「深圳招聘网」海量深圳人才招聘信息' in home_page.title
