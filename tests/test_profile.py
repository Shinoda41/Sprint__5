from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from Locators import Locators


class TestProfile:

    def test_profile_path(self, driver):

        entry_path = driver.find_element(*Locators.Entrance_from_reg)
        entry_path.click()
        email_input = driver.find_element(*Locators.Reg_Email)
        password_input = driver.find_element(*Locators.Reg_Password)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.Entry_button)
        entry.click()
        profile = driver.find_element(*Locators.Profile_button)
        profile.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.Order_history))
        order_history = driver.find_element(*Locators.Order_history)
        assert order_history.is_displayed()

    def test_logout_from_profile(self, driver):
        entry_path = driver.find_element(*Locators.Entrance_from_reg)
        entry_path.click()
        email_input = driver.find_element(*Locators.Reg_Email)
        password_input = driver.find_element(*Locators.Reg_Password)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.Entry_button)
        entry.click()
        profile = driver.find_element(*Locators.Profile_button)
        profile.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.Logout_button))
        logout = driver.find_element(*Locators.Logout_button)
        logout.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.Entry_button))
        entry = driver.find_element(*Locators.Entry_button)
        assert entry.is_displayed()
