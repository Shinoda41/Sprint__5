from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from Locators import Locators


class TestEntranceVariety:

    def test_entrance_main(self, driver):

        main_path = driver.find_element(*Locators.Main_logo)
        main_path.click()
        entry_path = driver.find_element(*Locators.Entrance_from_main)
        entry_path.click()
        email_input = driver.find_element(*Locators.Reg_Email)
        password_input = driver.find_element(*Locators.Reg_Password)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.Entry_button)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.Order_button))
        order_button = driver.find_element(*Locators.Order_button)
        assert order_button.is_displayed()

    def test_entrance_profile(self, driver):

        main_path = driver.find_element(*Locators.Main_logo)
        main_path.click()
        entry_path = driver.find_element(*Locators.Entrance_from_profile)
        entry_path.click()
        email_input = driver.find_element(*Locators.Reg_Email)
        password_input = driver.find_element(*Locators.Reg_Password)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.Entry_button)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.Order_button))
        order_button = driver.find_element(*Locators.Order_button)
        assert order_button.is_displayed()

    def test_entrance_reg(self, driver):

        entry_path = driver.find_element(*Locators.Entrance_from_reg)
        entry_path.click()
        email_input = driver.find_element(*Locators.Reg_Email)
        password_input = driver.find_element(*Locators.Reg_Password)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.Entry_button)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.Order_button))
        order_button = driver.find_element(*Locators.Order_button)
        assert order_button.is_displayed()

    def test_entrance_lost_password(self, driver):

        reg_path = driver.find_element(*Locators.Entrance_from_reg)
        reg_path.click()
        lost_password = driver.find_element(*Locators.Lost_Password)
        lost_password.click()
        entry_path = driver.find_element(*Locators.Entrance_from_lost_password)
        entry_path.click()
        email_input = driver.find_element(*Locators.Reg_Email)
        password_input = driver.find_element(*Locators.Reg_Password)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.Entry_button)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.Order_button))
        order_button = driver.find_element(*Locators.Order_button)
        assert order_button.is_displayed()
