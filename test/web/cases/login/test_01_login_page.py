# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: test_01_login_page.py
@time: 2024/5/28 20:12
"""

from pytest import assume

from test.web.cases import home_page, login_page


class TestLoginPage:
    @classmethod
    def setup_class(cls):
        print('\n===setup_class===')

    @classmethod
    def teardown_class(cls):
        print('\n===teardown_class===')

    def test_login(self):
        """测试登录"""
        home_page.get_header_component().login_or_sign_in()  # 主页点击登录/注册按钮
        login_page.login()  # 登录
        assert login_page.toast.text == "请先完成验证"

    def test_ui(self):
        """测试登录界面的UI元素"""
        with assume:
            assert login_page.iboss_call.text == '客户服务热线: 400 065 5799'
        with assume:
            assert login_page.header_logo.is_displayed()
        with assume:
            assert login_page.header_title.text == '找工作'
        with assume:
            assert login_page.header_description.text == '上BOSS直聘直接谈'
        with assume:
            assert login_page.communicate_icon.is_displayed()
        with assume:
            assert login_page.communicate_title.text == '沟通'
        with assume:
            assert login_page.communicate_description.text == '在线职位及时沟通'
        with assume:
            assert login_page.select_icon.is_displayed()
        with assume:
            assert login_page.select_title.text == '任性选'
        with assume:
            assert login_page.select_description.text == '各大行业职位任你选'

    def test_navigate_to_home(self):
        """测试导航到主页"""
        temp_home_page = login_page.navigate_to_home()  # 点击找工作图标
        assert temp_home_page.title == 'BOSS直聘-找工作上BOSS直聘直接谈！招聘求职找工作！'
