# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: base_page.py
@time: 2024/5/28 1:18
"""
import os
import sys

from poium import Page
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.utils import Utils


class WebDriverSingleton:
    _driver = None

    @staticmethod
    def get_driver_instance():
        if WebDriverSingleton._driver is None:
            driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                       '..', 'drivers', 'chromedriver.exe'))
            service = webdriver.ChromeService(executable_path=driver_path)
            WebDriverSingleton._driver = webdriver.Chrome(service=service)
        return WebDriverSingleton._driver


class BasePage(Page):
    def __init__(self, base_url=None):
        self.driver = WebDriverSingleton.get_driver_instance()
        self.config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                        '..', '..', '..', 'config', 'web_config.json'))
        if base_url is None:
            self.base_url = Utils.read_config(self.config_path)['base_url']
        else:
            self.base_url = base_url

        self.wait = WebDriverWait(self.driver, 10)
        self.open_home()

    def open_home(self):
        self.maximize_window()
        self.get(self.base_url)
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='https://www.zhipin.com/'][title='BOSS直聘']")))

    def quit(self):
        self.driver.quit()

    def maximize_window(self):
        self.driver.maximize_window()

    def minimize_window(self):
        self.driver.minimize_window()

    def press_key(self, key_str):
        key_code = getattr(Keys, key_str.upper())
        ActionChains(self.driver).send_keys(key_code).perform()

    def shift_key(self, key_str):
        ActionChains(self.driver).key_down(Keys.SHIFT).send_keys(key_str).perform()

    def ctrl_key(self, key_str):
        cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        ActionChains(self.driver).key_down(cmd_ctrl).send_keys(key_str).perform()

    def home(self):
        self.press_key('home')

    def end(self):
        self.press_key('end')

    def enter(self):
        self.press_key('enter')

    def swipe_up(self):
        pass

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()

    def current_url(self):
        return self.driver.current_url

    def get(self, url):
        self.driver.get(url)

    @property
    def title(self):
        return self.driver.title

    @property
    def alert(self):
        wait = WebDriverWait(self.driver, 3)
        return wait.until(lambda d: d.switch_to.alert)

    def send_keys_to_alert(self, text):
        self.alert.send_keys(text)

    def toast_text(self, selector):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector))).text
