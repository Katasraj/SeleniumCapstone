import allure
import pytest
import concurrent.futures
from selenium import webdriver
from tests.home.login_tests import *
from pages.home.login_page import LoginPage
from configfiles.location_path import Path_Login
from utilities.teststatus import TestStatus
import time


@pytest.mark.run(order=1)
@allure.description("With 5 users entering Username and Password concurrently")
def test_execute_concurrent_sessions():
    """
    Test function that runs Selenium tests in multiple threads.
    """

    @allure.step("Executing Threads")
    def run_test(session_name):
        try:
            # Initialize WebDriver and open the target URL
            driver = webdriver.Chrome()  # Replace with your WebDriver setup
            with allure.step("Opening the URL"):
                driver.get("https://www.letskodeit.com/")  # Replace with your login page URL

            # Initialize LoginTests and related dependencies in the thread
            # with allure.step("Initializing Login Tests"):
            #     test = LoginTests()
            #     test.lp = LoginPage(driver)  # Initialize LoginPage manually
            #     test.locator = Path_Login.login_element_location(test)
            #     test.ts = TestStatus(driver)  # Initialize TestStatus manually

            #with allure.step(f"Running {session_name}"):
            #     #test.test_invalidLogin()
                #LoginTests().test_validLogin()
                #test.test_validLogin()  # Execute the login test
            LoginTests().test_invalidLogin
            LoginTests().test_validLogin()

        except Exception as e:
            allure.attach(f"Exception: {str(e)}", name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            print(f"{session_name} raised an exception: {e}")

        finally:
            driver.quit()  # Close the browser after the test

    with allure.step("Execute tests in parallel"):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            sessions = [f"Session-{i}" for i in range(2)]  # Create 5 session names
            futures = [executor.submit(run_test, session) for session in sessions]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    allure.attach(f"Exception: {str(e)}", name="Exception Details",
                                  attachment_type=allure.attachment_type.TEXT)
                    print(f"Thread raised an exception: {e}")