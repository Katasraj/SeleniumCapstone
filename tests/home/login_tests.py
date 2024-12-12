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

''''
@pytest.mark.usefixtures("oneTimeSetUp","setUp"): This decorator tells pytest to use the fixtures named 
oneTimeSetUp and setUp before running any test cases in this class. Fixtures are functions that provide 
resources or perform setup tasks for tests.

@pytest.fixture(autouse=True): This decorator defines a fixture named classSetup that gets automatically 
used before every test case in this class. It takes another fixture oneTimeSetUp as an argument 
(likely for one-time browser setup) and assigns the result of LoginPage(self.driver) to the variable self.lp. 
This suggests the oneTimeSetUp fixture initializes the web driver instance (self.driver) needed for 
interacting with the login page.
'''

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
        time.sleep(2)
        #self.lp.ElementToWait(self.locator['signin_link'])
        # WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, self.locator['signin_link']))
        # )

        with allure.step("Clearing the login text field"):
            self.lp.clearItem(self.locator['emialLogin'],locatorType='xpath')


        with allure.step("Entering proper Username and Password"):
            self.lp.login('kotarinaga1@gmail.com', 'Katasraj111#')
        result1 = self.lp.verifyLoginTitle()

        time.sleep(5)
        with allure.step("Verifying Title"):
            self.ts.mark(result1,"Title Verified")
        result2 = self.lp.verifyLoginSuccessful()
        #self.lp.ElementToWait(self.locator['userIcon_After_login'])
        # WebDriverWait(self.driver, 30).until(
        #     EC.presence_of_element_located((By.XPATH, self.locator['my_courses']))
        # )
        self.ts.markFinal("test_ValidateLogin",result2,"Login Verification")
        #time.sleep(5)
        # self.lp.quitPage()

    @pytest.mark.run(order=1)
    @allure.step("Verifying with wrong credentials")
    def test_invalidLogin(self):
        #self.lp.logout()
        #self.lp.ElementToWait(self.locator['emialLogin'])
        with allure.step("Entering wrong password"):
            self.lp.login('kotarinaga1@gmail.com','Katasraj123#')
        result = self.lp.verifyLoginFailed()
        assert result == True