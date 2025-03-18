from pages.basepage import BasePage
import selenium.webdriver.support.expected_conditions as EC
import appium.webdriver.common.appiumby as BY
#-------操作原素----------
username_input = (BY.AppiumBy.ID,"")
password_input = (BY.AppiumBy.ID,"")
login_button = (BY.AppiumBy.ID,"")

class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def test_login(self,username,password):
        self.input_text(username_input, username)
        self.input_text(password_input,password)
        self.click(login_button)
        self.logger.info(f"执行登录操作")

        #页面同步跳转
        self.wait.until(EC.invisiblity_of_element_located(),30)

