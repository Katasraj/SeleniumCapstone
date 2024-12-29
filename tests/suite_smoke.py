import unittest

from tests.home.login_tests import LoginTests
from tests.courses.register_courses_tests import RegisterCoursesTests

'''Get all tests from the test classes'''
smt1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
smt2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesTests)


'''Create Test Suite by combining all test classes'''
smokeTest = unittest.TestSuite([smt1,smt2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)






