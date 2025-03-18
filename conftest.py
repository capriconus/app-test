import pytest
from appium import webdriver
from config.settings import andriod_caps, server_url


@pytest.fixture(scope='module')
def andriod_driver():
    caps = andriod_caps
    driver = webdriver.Remote(caps, server_url)
    yield driver
    driver.quit()