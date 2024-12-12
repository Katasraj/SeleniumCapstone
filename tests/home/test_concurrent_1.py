import allure
import concurrent.futures
from selenium import webdriver
from tests.home.test_login_concurrent import *
from pages.home.login_page import LoginPage
from configfiles.location_path import Path_Login
from utilities.teststatus import TestStatus

@allure.description("With 5 users entering Username and Password concurrently")
@allure.step("Executing Threads")
def execute_concurrent_sessions():
    # Function to run the login test
    def run_test(session_name):
        try:
            # Initialize WebDriver and open the target URL
            driver = webdriver.Chrome()  # Replace with your WebDriver setup
            #with allure.step("Openeing url"):
            driver.get("https://www.letskodeit.com/")  # Replace with your login page URL

            # Initialize LoginTests and related dependencies in the thread
            with allure.step("Validating Username and Password"):
                test = LoginTests()
            #test.driver = driver
            test.lp = LoginPage(driver)  # Initialize LoginPage manually
            test.locator = Path_Login.login_element_location(test)
            test.ts = TestStatus(driver)  # Initialize TestStatus manually

            with allure.step(f"Running {session_name}"):
                test.test_validLogin()  # Execute the login test

        except Exception as e:
            print(f"{session_name} raised an exception: {e}")

        finally:
            driver.quit()  # Close the browser after the test

    # Execute tests in parallel
    with allure.step("Execute tests in parallel"):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            sessions = [f"Session-{i}" for i in range(5)]  # Create 5 session names
            futures = [executor.submit(run_test, session) for session in sessions]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Thread raised an exception: {e}")

execute_concurrent_sessions()


# import concurrent.futures
# import allure
# from selenium import webdriver
# from tests.home.test_login_concurrent import *
# from pages.home.login_page import LoginPage
# from configfiles.location_path import Path_Login
# from utilities.teststatus import TestStatus
#
#
# @allure.description("With 5 users entering Username and Password concurrently")
# def test_concurrent_sessions():
#     """
#     Test function that runs Selenium tests in multiple threads.
#     """
#
#     @allure.step("Executing Threads")
#     def execute_concurrent_sessions():
#         # Function to run the login test
#         def run_test(session_name):
#             try:
#                 # Initialize WebDriver and open the target URL
#                 driver = webdriver.Chrome()  # Replace with your WebDriver setup
#                 driver.get("https://www.letskodeit.com/")  # Replace with your login page URL
#
#                 # Manually set up an instance of LoginTests
#                 test = LoginTests()
#                 test.driver = driver
#                 test.lp = LoginPage(driver)  # Initialize LoginPage manually
#                 test.locator = Path_Login.login_element_location(test)
#                 test.ts = TestStatus(driver)  # Initialize TestStatus manually
#
#                 with allure.step(f"Running {session_name}"):
#                     test.test_validLogin()  # Execute the login test
#
#             except Exception as e:
#                 print(f"{session_name} raised an exception: {e}")
#
#             finally:
#                 driver.quit()  # Close the browser after the test
#
#         # Execute tests in parallel
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             sessions = [f"Session-{i}" for i in range(5)]  # Create 5 session names
#             futures = [executor.submit(run_test, session) for session in sessions]
#             for future in concurrent.futures.as_completed(futures):
#                 try:
#                     future.result()
#                 except Exception as e:
#                     print(f"Thread raised an exception: {e}")
#
#     execute_concurrent_sessions()

# from tests.home.test_login_concurrent import *
# import concurrent.futures
# import allure
# from selenium import webdriver


# @allure.description("With 5 users entering Username and Password concurrently")
# def test_concurrent_sessions():
#     """
#     Test function that runs Selenium tests in multiple threads.
#     """
# @allure.description("With 5 users entering Username and Password concurrently")
# @allure.step("Executing Threads")
# def execute_concurrent_sessions():
#     # Function to run the login test
#     def run_test(session_name):
#         # Manually set up an instance of LoginTests
#         test = LoginTests()
#         test.driver = webdriver.Chrome()  # Replace with your WebDriver setup
#         test.driver.get('https://www.letskodeit.com/')
#         test.lp = LoginPage(test.driver)  # Initialize LoginPage manually
#         test.locator = Path_Login.login_element_location(test)
#         test.ts = TestStatus(test.driver)  # Initialize TestStatus manually
#
#         with allure.step(f"Running {session_name}"):
#             test.test_validLogin()  # Execute the login test
#
#         test.driver.quit()  # Close the browser after the test
#
#     # Execute tests in parallel
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         sessions = [f"Session-{i}" for i in range(1,5)]  # Create 5 session names
#         futures = [executor.submit(run_test, session) for session in sessions]
#         for future in concurrent.futures.as_completed(futures):
#             try:
#                 future.result()
#             except Exception as e:
#                 print(f"Thread raised an exception: {e}")
#
# execute_concurrent_sessions()


