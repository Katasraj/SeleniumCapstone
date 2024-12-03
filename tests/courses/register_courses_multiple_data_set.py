import unittest
import pytest
from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.teststatus import TestStatus
from ddt import ddt,data,unpack
import time


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self,oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("Javascript for beginners"),("Learn Python 3 from scratch"))
    def test_invalidEnrollment(self,courseName):
        self.courses.selectALlCourses()
        self.courses.enterCourseName(courseName)
        self.courses.enterSearchbuttonForCourse()
        time.sleep(5)
        self.courses.selectCourse()
        self.courses.clickonEnrollCourseButton()
        time.sleep(2)
        result = self.courses.findTextonCourse()
        self.ts.markFinal("test_invalidEnrollment",result,"Enrolled JS")
        time.sleep(2)
        self.courses.selectALlCourses()
        #self.courses.enrollCourse(num='1045 7956 1359 5688',exp='12/27',cvv='879')





