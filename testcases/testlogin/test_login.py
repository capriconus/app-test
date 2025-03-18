import allure
import pytest

from pages.loginpage import LoginPage
from utils.readyaml import readyaml

cases = readyaml('login.yaml')

class TestLogin:

    @pytest.mark.parametrize('logincase', cases)
    def test_login(self, logincase, driver):
        username_input = logincase['username']
        password_input = logincase['password']
        LoginPage(driver).input_text(username_input)
        allure.step("登录输入用户名")
        LoginPage(driver).input_text(password_input)
        allure.step("登录输入用户密码")
        LoginPage(driver).click()
        allure.step("点击登录")
        resp_msg = LoginPage(driver).get_msg()
        assert resp_msg, logincase['respmsg']




