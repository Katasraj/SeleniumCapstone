from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus


class LoginHelper:
    def execute_login(self, driver, locator):
        lp = LoginPage(driver)
        ts = TestStatus(driver)
        lp.clearItem(locator.login_element_location()['emialLogin'], locatorType='xpath')
        number_of_usrs = lp.get_username_password(locator.login_details())
        for iter in range(len(number_of_usrs)):
            lp.login(number_of_usrs[iter][0], number_of_usrs[iter][1])
            result1 = lp.verifyLoginTitle()
            ts.mark(result1, "Title Verified")
            result2 = lp.verifyLoginSuccessful()
            ts.markFinal("test_ValidateLogin", result2, "Login Verification")
