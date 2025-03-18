from pages.basepage import BasePage
import  appium.webdriver.common.appiumby as By


#-------页面原素---------
Welcome_Text = (By.AppiumBy.XPATH, "")


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_welcome_displayed(self):
        return self.find_element(Welcome_Text).isdisplayed()

