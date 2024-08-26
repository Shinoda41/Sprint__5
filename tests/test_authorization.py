from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from Locators import Locators


class TestEntranceVariety:

    def test_entrance_main(self, driver):

        main_path = driver.find_element(*Locators.MAIN_LOGO)
        main_path.click()
        entry_path = driver.find_element(*Locators.ENTRANCE_FROM_MAIN)
        entry_path.click()
        email_input = driver.find_element(*Locators.REG_EMAIL)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_entrance_profile(self, driver):

        main_path = driver.find_element(*Locators.MAIN_LOGO)
        main_path.click()
        entry_path = driver.find_element(*Locators.ENTRANCE_FROM_PROFILE)
        entry_path.click()
        email_input = driver.find_element(*Locators.REG_EMAIL)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_entrance_reg(self, driver):

        entry_path = driver.find_element(*Locators.ENTRANCE_FROM_REG)
        entry_path.click()
        email_input = driver.find_element(*Locators.REG_EMAIL)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_entrance_lost_password(self, driver):

        reg_path = driver.find_element(*Locators.ENTRANCE_FROM_REG)
        reg_path.click()
        lost_password = driver.find_element(*Locators.LOST_PASSWORD)
        lost_password.click()
        entry_path = driver.find_element(*Locators.ENTRANCE_FROM_LOST_PASSWORD)
        entry_path.click()
        email_input = driver.find_element(*Locators.REG_EMAIL)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert order_button.is_displayed()
