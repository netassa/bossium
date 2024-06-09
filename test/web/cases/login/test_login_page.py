# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: test_login_page.py
@time: 2024/5/28 20:12
"""
from test.web.pages.home_page import HomePage
from test.web.pages.login_page import LoginPage


class TestLoginPage:

    def test_login(self):
        home_page = HomePage()
        home_page.get_header_component().login_or_sign_in()
        login_page = LoginPage()
        login_page.login()
        assert login_page.toast.text == "请先完成验证"

    def test_ui(self):
        login_page = LoginPage()
        assert login_page.iboss_call.text == '客户服务热线: 400 065 5799'
        assert login_page.header_logo.is_displayed()
        assert login_page.header_title.text == '找工作'
        assert login_page.header_description.text == '上BOSS直聘直接谈'
        assert login_page.communicate_icon.is_displayed()
        assert login_page.communicate_title.text == '沟通'
        assert login_page.communicat_description.text == '在线职位及时沟通'
        assert login_page.select_icon.is_displayed()
        assert login_page.select_title.text == '任性选'
        assert login_page.select_description.text == '各大行业职位任你选'

    def test_navigate_to_home(self):
        login_page = LoginPage()
        home_page = login_page.navigate_to_home()
        assert home_page.title == 'BOSS直聘-找工作上BOSS直聘直接谈！招聘求职找工作！'


