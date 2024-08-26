import pytest
from selenium import webdriver

from data import Data
from helpers import Help


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(Data.BURGER_URL_REG)


    yield driver

    driver.quit()


def generated_user():
    return Help.generate_email()
