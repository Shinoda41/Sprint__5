from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from Locators import Locators


class TestProfile:

    def test_profile_path(self, driver):
        entry_path = driver.find_element(*Locators.ENTRANCE_FROM_REG)
        entry_path.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.REG_EMAIL))
        email_input = driver.find_element(*Locators.REG_EMAIL)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        profile = driver.find_element(*Locators.PROFILE_BUTTON)
        profile.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ORDER_HISTORY))
        order_history = driver.find_element(*Locators.ORDER_HISTORY)
        assert order_history.is_displayed()

    def test_logout_from_profile(self, driver):
        entry_path = driver.find_element(*Locators.ENTRANCE_FROM_REG)
        entry_path.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.REG_EMAIL))
        email_input = driver.find_element(*Locators.REG_EMAIL)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        profile = driver.find_element(*Locators.PROFILE_BUTTON)
        profile.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        logout = driver.find_element(*Locators.LOGOUT_BUTTON)
        logout.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ENTRY_BUTTON))
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        assert entry.is_displayed()
