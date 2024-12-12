from configfiles.location_path import Path_Login
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import allure
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.locator = Path_Login.login_element_location(self)

    @pytest.mark.run(order=1)
    @allure.step("Verifying with proper username/password credentials")
    def test_validLogin(self):
        time.sleep(2)
        # with allure.step("Clearing the login text field"):
        self.lp.clearItem(self.locator['emialLogin'], locatorType='xpath')

        # with allure.step("Entering proper Username and Password"):
        self.lp.login('kotarinaga1@gmail.com', 'Katasraj111#')
        result1 = self.lp.verifyLoginTitle()
        time.sleep(5)

        # with allure.step("Verifying Title"):
        #self.ts.mark(result1, "Title Verified")
        #result2 = self.lp.verifyLoginSuccessful()

# if  __name__ == "__main__":
#     LoginTests(unittest.TestCase).test_validLogin()



#@pytest.mark.usefixtures("test_setup")
# @allure.description("With 5 users Entering Username and Password and adding/removing an item from cart")
# def test_concurrent_sessions():
#     """
#     Test function that runs Selenium tests in multiple threads.
#     """
#     @allure.step("Executing Threads")
#     def execute_concurrent_sessions():
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             # Create session names for identification
#             sessions = [f"Session-{i}" for i in range(5)]
#             # Each thread runs `run_test`
#             executor.map(run_test, sessions)
#
#     execute_concurrent_sessions()


#//button[contains(text(),'Add to cart')]

#//div[contains(text(),'Sauce Labs Backpack')]/../../..//div[@class='pricebar']//button
#//div[contains(text(),'Sauce Labs Backpack')]/../../..//button