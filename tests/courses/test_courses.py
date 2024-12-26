import unittest
import pytest
from pages.courses.register_courses_pages import RegisterCoursesPage
from configfiles.location_filename import FileLocation
from utilities.teststatus import TestStatus
from ddt import ddt, data
from utilities.read_data import ReadData
from API_Calls.POST_call_setup import *
import allure
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetUp(self):
        self.course = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        #self.nav = NavigationPage(self.driver)


    @pytest.mark.dependency(name="verify_courses")
    @allure.step("Validating courses by reading from CSV file and inserting in MySQL Database")
    def test_verifyMultipleCourses(self):
        courses_and_prices = ReadData(FileLocation().csv_location()[0]).getCombinedData()
        #courses_and_prices = ReadData("F:\\PycharmProjects\\SeleniumCapstone\\configfiles\\testdata.csv").getCombinedData()
        for courseName, price in courses_and_prices:
            with allure.step(f"Step 1: Searching for a course {courseName}"):
                self.course.selectALlCourses()
                self.course.enterCourseName(courseName)
                self.course.enterSearchbuttonForCourse()
                time.sleep(5)
            with allure.step(f"Step 2: Selecting and enrolling the course {courseName}"):
                self.course.selectCourse()
                self.course.clickonEnrollCourseButton()
                time.sleep(3)
            with allure.step(f"Step 3: Verifying course {courseName} enrollment"):
                result = self.course.findTextonCourse(courseName)
                # assert courseName in result, f"Expected text '{courseName}' found in '{result}'"
                time.sleep(3)
                self.ts.markFinal("test_verifyMultipleCourses", result, courseName)

# class DeletingCSVDataTests(unittest.TestCase):
#     @pytest.mark.run(order=1)
#     def test_delete_courses_in_database(self):
#         APIServer(FileLocation().csv_location()[0]).delete_courses_from_db()

class InsertingCSVDataTests(unittest.TestCase):
    @pytest.mark.dependency(depends=["verify_courses"])
    def test_insert_in_database(self):
        with allure.step("Inserting data into the database from CSV file"):
            #APIServer().delete_courses_from_db()
            APIServer(FileLocation().csv_location()[0])._course_delete_insert()
            allure.attach("Database operation completed successfully", name="DB Insertion Details",
                          attachment_type=allure.attachment_type.TEXT)

class GetEnrolledCourses(unittest.TestCase):
    @pytest.mark.dependency(depends=["verify_courses"])
    def test_get_courses(self):
        with allure.step("Getting EnrolledCourses"):
            #APIServer().delete_courses_from_db()
            APIServer().get_courses_from_db()


if __name__ == "__main__":
    # Create test suite
    suite = unittest.TestSuite()
    #suite.addTest(DeletingCSVDataTests("test_delete_courses_in_database"))
    suite.addTest(RegisterCoursesCSVDataTests("test_verifyMultipleCourses"))
    suite.addTest(InsertingCSVDataTests("test_insert_in_database"))
    suite.addTest(GetEnrolledCourses("test_get_courses"))
    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)

'''
test_insert_in_database will only run after test_verifyMultipleCourses passes, ensuring proper test flow.
'''