# import unittest
# import pytest
# from pages.courses.register_courses_pages import RegisterCoursesPage
# from pages.home.navigation_page import NavigationPage
# from utilities.teststatus import TestStatus
# from ddt import ddt,data,unpack
# from utilities.read_data import ReadData
# #from utilities.read_data import getCSVData
# import allure
# import time
#
#
# @pytest.mark.usefixtures("oneTimeSetUp","setUp")
# @ddt
# class RegisterCoursesCSVDataTests(unittest.TestCase):
#     @pytest.fixture(autouse=True)
#     def objectSetUp(self):
#         self.courses = RegisterCoursesPage(self.driver)
#         self.ts = TestStatus(self.driver)
#         self.nav = NavigationPage(self.driver)
#
#     def setUp(self):
#         self.nav.navigateToALlCourses()
#
#     # @pytest.mark.run(order=1)
#     # @allure.description("Validating courses by reading from csv file")
#     # #@data(("Javascript for beginners"),("Learn Python 3 from scratch"))
#     # @data(*ReadData("F:\\PycharmProjects\\SeleniumCapstone\\testdata.csv").getCSVData())
#     # #@unpack
#     # def test_verifyMultipleCourses(self,courseName):
#     #     print("courseName*************",courseName)
#
#     print(100*'*')
#     @pytest.mark.run(order=1)
#     @data(*ReadData("/configfiles/testdata.csv").getCombinedData())
#     @unpack
#     def test_prices(self,combined_data):
#         for c,p in combined_data:
#             print("COURESE--------------",c)
#             print("Price--------------", p)
#
