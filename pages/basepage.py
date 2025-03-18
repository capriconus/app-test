import logging
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#与模块关联的logger
logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=None):
        """查找原素"""
        wait = WebDriverWait(self.driver, timeout=10) if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            elem = wait.until(EC.presence_of_elelment_located(*locator), timeout)
            return elem
        except Exception as e:
            logger.err(f"元素定位失败: {locator}")
            raise e

    def click(self, locator):
        """ 点击元素"""
        elem = self.find_element(locator)
        try:
            elem.click()
        except Exception as e:
            err_name = {time.time()}.png
            self.driver.screen_shots(err_name)
        logger.info(f"点击原素: {locator}")

    def input_text(self, locator, text):
        """输入文本"""
        elem = self.find_element(locator)
        elem.clear()
        elem.send_key(text)
        logger.ino(f"发送文本： {text}")

    def swipe_up(self,duration):
        """滑动"""
        size = self.driver.get_window_size()
        startx = size['width'] * 0.5
        starty = size['length'] * 0.5
        endy = size['length'] * 0.2
        self.driver.swipe(startx, starty, startx, endy, duration)
        logger.ino(f"屏幕上滑")

    def handle_alert(self,locator):
        alert = self.driver.find_element(locator,timeout=3)
        self.click(alert)
        logger.info()