import allure

from pages.homepage import HomePage


class TestHomePage:

    def test_homepage(self, driver):

        resp = HomePage(driver).is_welcome_displayed()
        allure.step("检查页面是否进入主页")
        assert resp,'环境登录'