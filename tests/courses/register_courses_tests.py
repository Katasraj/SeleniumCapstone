import unittest
import pytest
from pages.courses.register_courses_pages import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import allure
import time


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self,oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    @allure.description("Validating course by entering course name in search box")
    def test_invalidEnrollment(self):
        self.courses.selectALlCourses()
        self.courses.enterCourseName('javascript')
        self.courses.enterSearchbuttonForCourse()
        time.sleep(5)
        self.courses.selectCourse()
        self.courses.clickonEnrollCourseButton()
        time.sleep(2)
        result = self.courses.findTextonCourse()
        print("JS RESULT ************: ",result)
        self.ts.markFinal("test_invalidEnrollment",result,"Enrolled JS")
        #self.courses.enrollCourse(num='1045 7956 1359 5688',exp='12/27',cvv='879')
        self.nav.navigateToALlCourses()





