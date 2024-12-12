import concurrent.futures
import unittest
import allure
import time
from tests.home.login_tests import LoginTests


def run_login_test(session_name):
    start_time = time.time()

    con = unittest.TestLoader().loadTestsFromTestCase(LoginTests)

    regressionTest = unittest.TestSuite([con])
    unittest.TextTestRunner(verbosity=2).run(regressionTest)

    print(f"{session_name}: Test completed successfully")
    end_time = time.time()
    print(f"Page Load Time for {session_name}: {end_time - start_time} seconds")

@allure.description("With 2 users Entering Username and Password")
def test_concurrent_sessions():
    """
    Test function that runs Selenium tests in multiple threads.
    """
    @allure.step("Executing Threads")
    def execute_concurrent_sessions():
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Create session names for identification
            sessions = [f"Session-{i}" for i in range(2)]
            # Each thread runs `run_test`
            executor.map(run_login_test, sessions)

    execute_concurrent_sessions()