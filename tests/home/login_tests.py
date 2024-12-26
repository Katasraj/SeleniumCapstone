from configfiles.location_path import Path_Login
from pages.home.helper import LoginHelper
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import allure
import time

''''
@pytest.mark.usefixtures("oneTimeSetUp","setUp"): This decorator tells pytest to use the fixtures named 
oneTimeSetUp and setUp before running any test cases in this class. Fixtures are functions that provide 
resources or perform setup tasks for tests.

@pytest.fixture(autouse=True): This decorator defines a fixture named classSetup that gets automatically 
used before every test case in this class. It takes another fixture oneTimeSetUp as an argument 
(likely for one-time browser setup) and assigns the result of LoginPage(self.driver) to the variable self.lp. 
This suggests the oneTimeSetUp fixture initializes the web driver instance (self.driver) needed for 
interacting with the login page.

By creating a pytest.ini file in the project root and defining the pythonpath setting, you ensure that all 
test_*.py files across your project can locate and use the conftest.py file, regardless of their location.

Here's why this works:
pytest.ini is a configuration file recognized by pytest. When you define the pythonpath setting in it, 
pytest automatically adds the specified directory (in your case, configfiles) to the PYTHONPATH.
Since the conftest.py file is now in a directory that is included in the PYTHONPATH, pytest can discover 
and use the fixtures, hooks, and options defined in it.

Driver Initialization:

The WebDriver instance (self.driver) is created in the oneTimeSetUp fixture and shared with the LoginTests class.
Locator Initialization:

self.locator is initialized in the objectSetup method for every test.
Dynamic Test Logic:

The LoginHelper.execute_login method receives driver and locator dynamically, making it reusable across 
tests and threads.

pytest -n 5 -vv .\login_tests.py
The -n option specifies the number of parallel workers. In your case, -n 5 will run the tests across 5 workers


How self.driver Is Set:

The oneTimeSetUp fixture creates the driver and assigns it to the request.cls.driver attribute.
The LoginTests class accesses self.driver, which is set by the oneTimeSetUp fixture.
Autouse Fixture:

The objectSetup method is an autouse=True fixture. This ensures it automatically runs for every test method in the class.
Remove Explicit Parameters:

Do not explicitly pass oneTimeSetUp to objectSetup or any test methods; pytest.mark.usefixtures takes care of it.
'''

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):
        # self.locator = Path_Login()  # Locator initialization
        # self.helper = LoginHelper()  # LoginHelper initialization
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        #self.locator = Path_Login.login_element_location(self)
        self.locator = Path_Login()

    # @pytest.mark.run(order=2)
    # @allure.step("Verifying with proper username/password credentials")
    # def test_validLogin(self):
    #     time.sleep(2)
    #     self.helper.execute_login(self.driver, self.locator)

    @pytest.mark.run(order=2)
    @allure.step("Verifying with proper username/password credentials")
    def test_validLogin(self):
        time.sleep(2)
        self.lp.clearItem(self.locator.login_element_location()['emialLogin'],locatorType='xpath')
        number_of_usrs = self.lp.get_username_password(self.locator.login_details())
        for iter in range(len(number_of_usrs)):
            self.lp.login(number_of_usrs[iter][0],number_of_usrs[iter][1])
            result1 = self.lp.verifyLoginTitle()
            self.ts.mark(result1,"Title Verified")
            result2 = self.lp.verifyLoginSuccessful()
            time.sleep(5)
            self.ts.markFinal("test_ValidateLogin",result2,"Login Verification")

    @pytest.mark.run(order=1)
    @allure.step("Verifying with wrong credentials")
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login('kotarinaga1@gmail.com','Katasraj123#')
        result = self.lp.verifyLoginFailed()
        assert result == True