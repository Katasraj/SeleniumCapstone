import time

import pytest
from pages.courses.register_courses_pages import RegisterCoursesPage
from configfiles.location_filename import FileLocation
from utilities.teststatus import TestStatus
from utilities.read_data import ReadData
from API_Calls.POST_call_setup import APIServer
from utilities.util import Util
import allure
import logging
import utilities.custom_logger as cl

"""Class to test course registration functionality"""
@pytest.mark.usefixtures("oneTimeSetUp")
class TestRegisterCoursesCSVData:
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetUp(self):
        """Set up the page object and test utilities"""
        self.course = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.regression
    @pytest.mark.dependency(name="test_check_multiple_courses")
    @pytest.mark.run(order=2)
    @allure.description("Validating courses by reading from CSV file and inserting in MySQL Database")
    def test_check_multiple_courses(self):
        """Test to verify multiple courses from a CSV file"""
        courses_and_prices = ReadData(FileLocation().csv_location()[0]).getCombinedData()
        for course_name, price in courses_and_prices:
            retry_count = 0
            max_retries = 3  # Retry up to 3 times
            while retry_count < max_retries:
                try:

                    with allure.step(f"Step 1: Searching for a course {course_name}"):
                        self.course.selectALlCourses()
                        self.course.enterCourseName(course_name)
                        self.course.enterSearchbuttonForCourse()
                        Util().sleep(5, info="Selecting and enrolling in the course")
                        course_name_on_page = self.course.get_enrolled_course_name(course_name)
                        print("course_name_on_page",course_name_on_page)
                        assert course_name == course_name_on_page,f"Course Names are not equal. Expected:{course_name_on_page},Actual: {course_name}"
                    with allure.step(f"Step 2: Selecting and enrolling in the course {course_name}"):
                        self.course.selectCourse()
                        self.course.clickonEnrollCourseButton()
                        Util().sleep(5, info="Verifying for course")
                    with allure.step(f"Step 3: Verifying course {course_name} enrollment"):
                        courseName_result = self.course.findTextonCourse(course_name)
                        #assert course_name == courseName_result[0],f"Course Names are not equal. Expected: {courseName_result[0]}, Actual: {course_name}"
                        print("COURSE ********",courseName_result[0])
                        Util().sleep(5, info="Verifying for multiple course")
                        self.ts.markFinal("test_verify_multiple_courses", courseName_result[1], course_name)
                        break
                except AssertionError as e:
                    retry_count += 1
                    allure.attach(
                        f"Retry {retry_count}: Exception: {str(e)}",
                        name="Retry Details",
                        attachment_type=allure.attachment_type.TEXT
                    )
                    if retry_count < max_retries:
                        with allure.step(f"Retrying for course '{course_name}'"):
                            print(f"Retrying for course '{course_name}' ({retry_count}/{max_retries})...")
                            continue  # Retry again
                    else:
                        with allure.step(f"Max retries reached for course '{course_name}'"):
                            print(f"Max retries reached for course '{course_name}'. Failing test.")
                            raise e  # Re-raise exception after max retries

class TestInsertCSVData:
    """Class to test database insertion"""
    log = cl.customLogger(logging.DEBUG)

    @pytest.mark.regression
    @pytest.mark.dependency(depends=["test_check_multiple_courses"])
    @pytest.mark.run(order=3)
    @allure.description("Inserting data from CSV file into the database")
    def test_insert_in_database(self):
        """Test to insert CSV data into the database"""
        try:
            with allure.step("Inserting data into the database from the CSV file"):
                # Perform the database insertion operation
                self.log.info("Initially delete courses from db and insert once it's enrolled")
                APIServer(FileLocation().csv_location()[0])._course_delete_insert()
                allure.attach("Database operation completed successfully",
                              name="DB Insertion Details",
                              attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            # Attach the error to the Allure report for debugging
            allure.attach(f"Exception occurred: {str(e)}",
                          name="Database Insertion Exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        assert True