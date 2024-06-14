# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: base_page.py
@time: 2024/5/28 1:18
"""
import os
import sys
import time

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
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            WebDriverSingleton._driver = webdriver.Chrome(service=service, options=options)
        return WebDriverSingleton._driver


class BasePage(Page):
    driver = None
    if driver is None:
        driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                       '..', 'drivers', 'chromedriver.exe'))
        service = webdriver.ChromeService(executable_path=driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=service, options=options)
    _config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                        '..', '..', '..', 'config', 'web_config.json'))
    _base_url = Utils.read_config(_config_path)['base_url']
    _opened_home = True

    def __init__(self):
        super().__init__(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        if BasePage._opened_home:
            self._open_home()
            BasePage._opened_home = False

    def _open_home(self):
        self.get(self._base_url)
        self.wait_for_element_to_be_visible(By.CSS_SELECTOR, "a[href='https://www.zhipin.com/'][title='BOSS直聘']")

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

    def get_element(self, locator_type, locator):
        time.sleep(0.5)
        return self.wait.until(EC.visibility_of_element_located((locator_type, locator)))

    def get_elements(self, locator_type, locator):
        time.sleep(0.5)
        return self.wait.until(EC.visibility_of_all_elements_located((locator_type, locator)))

    def wait_for_element_to_be_visible(self, locator_type, locator):
        self.wait.until(EC.visibility_of_element_located((locator_type, locator)))

    def wait_for_element_to_be_invisible(self, locator_type, locator):
        self.wait.until(EC.invisibility_of_element((locator_type, locator)))

    def wait_for_page_is_loaded(self):
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def go_to_my_page(self):
        self.driver.get(self._base_url)
        time.sleep(0.5)

