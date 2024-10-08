from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from Locators import Locators


class TestConstructor:

    def test_constructor_from_profile(self, driver):
        entry_path = driver.find_element(*Locators.ENTRANCE_FROM_REG)
        entry_path.click()
        email_input = driver.find_element(*Locators.REG_EMAIL)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        entry.click()
        profile = driver.find_element(*Locators.PROFILE_BUTTON)
        profile.click()
        constructor = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        constructor.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_constructor_by_main_logo_from_profile(self, driver):
        entry_path = driver.find_element(*Locators.ENTRANCE_FROM_REG)
        entry_path.click()
        email_input = driver.find_element(*Locators.REG_EMAIL)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        entry.click()
        profile = driver.find_element(*Locators.PROFILE_BUTTON)
        profile.click()
        main_path = driver.find_element(*Locators.MAIN_LOGO)
        main_path.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_constructor_parts_sauces(self, driver):
        entry_path = driver.find_element(*Locators.ENTRANCE_FROM_REG)
        entry_path.click()
        email_input = driver.find_element(*Locators.REG_EMAIL)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SAUCES_BUTTON))
        sauce_button = driver.find_element(*Locators.SAUCES_BUTTON)
        sauce_button.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SAUCES))
        sauces = driver.find_element(*Locators.SAUCES)
        assert sauces.is_displayed()

    def test_constructor_parts_buns(self, driver):
        entry_path = driver.find_element(*Locators.ENTRANCE_FROM_REG)
        entry_path.click()
        email_input = driver.find_element(*Locators.REG_EMAIL)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SAUCES_BUTTON))
        sauce_button = driver.find_element(*Locators.SAUCES_BUTTON)
        sauce_button.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.BUNS_BUTTON))
        buns_button = driver.find_element(*Locators.BUNS_BUTTON)
        buns_button.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.BUNS))
        buns = driver.find_element(*Locators.BUNS)
        assert buns.is_displayed()

    def test_constructor_parts_toppings(self, driver):
        entry_path = driver.find_element(*Locators.ENTRANCE_FROM_REG)
        entry_path.click()
        email_input = driver.find_element(*Locators.REG_EMAIL)
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        email_input.send_keys(Data.AUTH_EMAIL)
        password_input.send_keys(Data.AUTH_PASSWORD)
        entry = driver.find_element(*Locators.ENTRY_BUTTON)
        entry.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.TOPPINGS_BUTTON))
        toppings_button = driver.find_element(*Locators.TOPPINGS_BUTTON)
        toppings_button.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.TOPPINGS))
        toppings = driver.find_element(*Locators.TOPPINGS)
        assert toppings.is_displayed()
