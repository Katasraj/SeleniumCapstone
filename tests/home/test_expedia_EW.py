from configfiles.location_path import Path_Login
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.locator = Path_Login.login_element_location(self)

    @pytest.mark.run(order=2)
    @allure.step("Verifying with proper username/password credentials")
    def test_validLogin(self):
        # Wait for the page to completely load
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        with allure.step("Clearing the login text field"):
            self.lp.clearItem(self.locator['emialLogin'], locatorType='xpath')

        with allure.step("Entering proper Username and Password"):
            self.lp.login('kotarinaga1@gmail.com', 'Katasraj111#')
        result1 = self.lp.verifyLoginTitle()

        with allure.step("Verifying Title"):
            self.ts.mark(result1, "Title Verified")

        # Wait for the user icon to be visible after login
        # WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located((By.XPATH, self.locator['userIcon_After_login']))
        # )

        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_ValidateLogin", result2, "Login Verification")

    @pytest.mark.run(order=1)
    @allure.step("Verifying with wrong credentials")
    def test_invalidLogin(self):
        # self.lp.logout()
        # self.lp.ElementToWait(self.locator['emialLogin'])
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        with allure.step("Entering wrong password"):
            self.lp.login('kotarinaga1@gmail.com', 'Katasraj123#')
        result = self.lp.verifyLoginFailed()
        assert result == True