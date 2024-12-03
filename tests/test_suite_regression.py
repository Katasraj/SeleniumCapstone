import unittest

from tests.courses.register_courses_csv_data import RegisterCoursesCSVDataTests

'''Get all tests from the test classes'''
reg1 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

'''Create Test Suite by combining all test classes'''

regressionTest = unittest.TestSuite([reg1])
unittest.TextTestRunner(verbosity=2).run(regressionTest)



