# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: login_page.py
@time: 2024/5/28 20:00
"""
from poium import Element

from test.web.pages.base_page import BasePage
from test.web.pages.home_page import HomePage
from utils.utils import Utils


class LoginPage(BasePage):
    _base_url = 'https://www.zhipin.com/web/user/?ka=header-login'

    # 左边图标区
    header_logo = Element('a[ka="header-logo"]')
    header_title = Element('a[ka="header-logo"] div em')
    header_description = Element('a[ka="header-logo"] div p')

    communicate_icon = Element('.icon-chat')
    communicate_title = Element(".icon-chat+em")
    communicate_description = Element(".icon-chat~span")

    select_icon = Element('.icon-select')
    select_title = Element(".icon-select+em")
    select_description = Element(".icon-select~span")

    # 中央登录区
    user_name_input = Element("input[placeholder='手机号']")
    verify_code_input = Element("input[placeholder='短信验证码']")
    policy_checkbox = Element("input[type='checkbox']")
    submit = Element("button[type='submit']")
    toast = Element(".toast-con")

    # 右边区域
    iboss_call = Element(xpath="//div[@class='tel']")

    def __init__(self, user_name=None, verify_code=None):
        super().__init__()
        if user_name is None:
            self.user_name = Utils.read_config(self._config_path)['user_name']
        else:
            self.user_name = user_name
        if verify_code is None:
            self.verify_code = Utils.read_config(self._config_path)['verify_code']
        else:
            self.verify_code = verify_code

    def login(self, user_name=None, verify_code=None):
        if user_name is None:
            user_name = self.user_name

        if verify_code is None:
            verify_code = self.verify_code

        self.user_name_input.send_keys(user_name)
        self.verify_code_input.send_keys(verify_code)
        self.policy_checkbox.click()
        self.submit.click()

    def navigate_to_home(self):
        self.header_logo.click()
        return HomePage()
