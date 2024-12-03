import unittest
import pytest
from pages.courses.register_courses_pages import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
from ddt import ddt,data,unpack
from utilities.read_data import getCSVData
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
    @data(*getCSVData("F:\\PycharmProjects\\LetsKodeIt_2\\testdata.csv"))
    def test_verifyMultipleCourses(self,courseName):
        self.courses.selectALlCourses()
        self.courses.enterCourseName(courseName)
        self.courses.enterSearchbuttonForCourse()
        time.sleep(5)
        self.courses.selectCourse()
        self.courses.clickonEnrollCourseButton()
        time.sleep(2)
        result = self.courses.findTextonCourse()
        self.ts.markFinal("test_verifyMultipleCourses",result,"Enrolled JS")
        time.sleep(2)

        #self.courses.enrollCourse(num='1045 7956 1359 5688',exp='12/27',cvv='879')





