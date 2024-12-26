from pages.courses.register_courses_pages import RegisterCoursesPage
from configfiles.location_filename import FileLocation
from utilities.read_data import ReadData
from utilities.teststatus import TestStatus
from configfiles.location_path import Path_Login
from pages.home.login_page import LoginPage
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
        self.courses = RegisterCoursesPage(self.driver)
        self.locator = Path_Login.login_element_location(self)
        self.login_creds = Path_Login.single_user_login_details(self)

    @pytest.mark.run(order=1)
    @allure.step("Login with username and password")
    def test_Login_to_page(self):
        time.sleep(2)
        self.lp.clearItem(self.locator['emialLogin'], locatorType='xpath')
        with allure.step("Login with credentials"):
            self.lp.login(self.login_creds['username'], self.login_creds['password'])
        self.lp.verifyLoginTitle()
        with allure.step("Verifying Login successful"):
            self.lp.verifyLoginSuccessful()
        time.sleep(3)

        coursedetails = ReadData(FileLocation().csv_location()[1]).get_dropdownCourses()

        for courseName in coursedetails:
            retry_count = 0
            max_retries = 3  # Retry up to 3 times

            while retry_count < max_retries:
                try:
                    with allure.step("Selecting All Courses Tab"):
                        self.courses.selectALlCourses()
                    time.sleep(2)
                    with allure.step(f"Selecting Course {courseName} from dropdown"):
                        self.courses.selectDropDownCourse(courseName)
                        time.sleep(3)
                        result = self.courses.verifyCourseCategory(courseName)

                        course_name_from_page = self.courses.course_category_name(courseName)
                        course_name_from_page = course_name_from_page.split("Category : ")[1].strip()
                        time.sleep(2)

                        # Assert if course name matches
                        self.assertEqual(
                            courseName,
                            course_name_from_page,
                            f"Course '{courseName}' not matching"
                        )

                        # Mark as final if successful
                        self.ts.markFinal("test_Login_to_page", result, "Course Category Verification")
                        break  # Exit retry loop if successful

                except AttributeError as e:
                    retry_count += 1
                    allure.attach(
                        f"Retry {retry_count}: Exception: {str(e)}",
                        name="Retry Details",
                        attachment_type=allure.attachment_type.TEXT
                    )
                    if retry_count < max_retries:
                        with allure.step(f"Retrying for course '{courseName}'"):
                            print(f"Retrying for course '{courseName}' ({retry_count}/{max_retries})...")
                            continue  # Retry again
                    else:
                        with allure.step(f"Max retries reached for course '{courseName}'"):
                            print(f"Max retries reached for course '{courseName}'. Failing test.")
                            raise e  # Re-raise exception after max retries
