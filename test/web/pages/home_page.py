# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: home_page.py
@time: 2024/5/28 19:49
"""

from test.web.pages.base_page import BasePage
from test.web.pages.common_component_page import HeaderPage, FooterPage


class HomePage(BasePage):
    _base_url = 'https://www.zhipin.com/'

    def get_header_component(self):
        return HeaderPage()

    def get_footer_component(self):
        return FooterPage()
