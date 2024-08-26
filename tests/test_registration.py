from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from helpers import Help
from Locators import Locators


class TestRegistration:

    def test_registration_incorrect_password(self, driver):

        generated_email = Help.generate_email()

        email_input = driver.find_element(*Locators.REG_EMAIL)
        name_input = driver.find_element(*Locators.REG_NAME)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        reg_button = driver.find_element(*Locators.REG_BUTTON)

        email_input.send_keys(generated_email)
        name_input.send_keys(Data.AUTH_NAME)
        password_input.send_keys(Data.WRONG_PASSWORD)
        reg_button.click()
        password_info = driver.find_element(*Locators.WRONG_PASSWORD_INFO)
        assert password_info.is_displayed()

    def test_registration(self, driver):

        generated_email = Help.generate_email()

        email_input = driver.find_element(*Locators.REG_EMAIL)
        name_input = driver.find_element(*Locators.REG_NAME)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        reg_button = driver.find_element(*Locators.REG_BUTTON)

        name_input.send_keys(Data.AUTH_NAME)
        email_input.send_keys(generated_email)
        password_input.send_keys(Data.AUTH_PASSWORD)
        reg_button.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ENTRANCE))
        entrance_stage = driver.find_element(*Locators.ENTRANCE)
        assert entrance_stage.is_displayed()
