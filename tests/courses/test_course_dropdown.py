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
        #result1 = self.lp.verifyLoginTitle()
        #self.ts.mark(result1, "Title Verified")
        with allure.step("Verifying Login successful"):
            self.lp.verifyLoginSuccessful()
            #result = self.lp.verifyLoginSuccessful()
        time.sleep(3)
        #self.ts.markFinal("test_ValidateLogin", result, "Login Verification")
        coursedetails = ReadData(FileLocation().csv_location()[1]).get_dropdownCourses()
        for courseName in coursedetails:
            with allure.step("Selecting All Courses Tab"):
                self.courses.selectALlCourses()
            # time.sleep(2)
            # self.courses.selectCategory()
            time.sleep(2)
            # self.courses.verifyElement()
            with allure.step(f"Selecting Course {courseName} from dropdown"):
                self.courses.selectDropDownCourse(courseName)
                time.sleep(3)
                result = self.courses.verifyCourseCategory(courseName)
                #print("Course CAT NameL: ", result)
                course_name_from_page = self.courses.course_category_name(courseName)
                course_name_from_page = course_name_from_page.split("Category : ")[1].strip()
                time.sleep(2)
                #print("Course CAT NameL: ",course_name_from_page)
                self.assertEqual(courseName,course_name_from_page,f"Course '{courseName}' not matching")
                self.ts.markFinal("test_Login_to_page", result, "Course Category Verification")





