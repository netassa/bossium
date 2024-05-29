# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: login_page.py
@time: 2024/5/28 20:00
"""
from poium import Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from test.web.pages.base_page import BasePage
from utils.utils import Utils


class LoginPage(BasePage):
    user_name_input = Element("input[placeholder='手机号']")
    verify_code_input = Element("input[placeholder='短信验证码']")
    policy_checkbox = Element("input[type='checkbox']")
    submit = Element("button[type='submit']")
    toast = Element(".toast-con")

    def __init__(self, base: BasePage = None, user_name=None, verify_code=None):
        self.driver = base.driver
        self.wait = base.wait
        config_path = base.config_path
        if user_name is None:
            self.user_name = Utils.read_config(config_path)['user_name']
        else:
            self.user_name = user_name
        if verify_code is None:
            self.verify_code = Utils.read_config(config_path)['verify_code']
        else:
            self.verify_code = verify_code
        login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-login-btn")))
        login_button.click()

    def login(self, user_name=None, verify_code=None):
        if user_name is None:
            user_name = self.user_name

        if verify_code is None:
            verify_code = self.verify_code

        self.user_name_input.send_keys(user_name)
        self.verify_code_input.send_keys(verify_code)
        self.policy_checkbox.click()
        self.submit.click()
