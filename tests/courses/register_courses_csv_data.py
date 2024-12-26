import unittest
import pytest

from configfiles.location_filename import FileLocation
from pages.courses.register_courses_pages import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
from ddt import ddt,data,unpack
from utilities.read_data import ReadData
from API_Calls.POST_call_setup import *
import allure
import time

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetUp(self):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToALlCourses()

    @pytest.mark.run(order=1)
    @allure.description("Validating courses by reading from csv file")
    #@data(("Javascript for beginners"),("Learn Python 3 from scratch"))
    @data(*ReadData(FileLocation().csv_location()[0]).getCSVData())
    def test_verifyMultipleCourses(self,courseName):
        with allure.step("Step 1: Searching for a course"):
            self.courses.selectALlCourses()
            self.courses.enterCourseName(courseName)
            self.courses.enterSearchbuttonForCourse()
            time.sleep(5)

        with allure.step("Step 2: Selecting and enrolling in the course"):
            self.courses.selectCourse()
            self.courses.clickonEnrollCourseButton()
            time.sleep(3)

        with allure.step("Step 3: Verifying course enrollment"):
            result = self.courses.findTextonCourse()
            time.sleep(3)
            self.ts.markFinal("test_verifyMultipleCourses",result,courseName)

    # @pytest.mark.run(order=2)
    # @allure.description("Inserting data into the database from CSV file")
    # def test_insert_in_database(self):
    #     with allure.step("Connecting to API and inserting data into the database"):
    #         APIServer("F:\\PycharmProjects\\SeleniumCapstone\\testdata.csv").insert_course()


class InsertingCSVDataTests(unittest.TestCase):
    @pytest.mark.run(order=2)
    @allure.step("Inserting data into the database from CSV file")
    def test_insert_in_database(self):
        APIServer("/configfiles/testdata.csv").insert_course()



    #@pytest.mark.run(order=2)
    # @allure.description("Inserting data into the database from CSV file")
    # def test_insert_in_database(self):
    #     # Read courses and prices dynamically and update the database
    #     courses_and_prices = ReadData("F:\\PycharmProjects\\SeleniumCapstone\\testdata.csv").getCombinedData()
    #     for courseName, price in courses_and_prices:
    #         print(f"Inserting course: {courseName} with price: {price}")
    #         APIServer(courseName, price).use_api_server()






