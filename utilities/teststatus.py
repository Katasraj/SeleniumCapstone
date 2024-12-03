import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):

        super(TestStatus,self).__init__(driver)
        self.resultList = []

    def setResult(self,result,resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append('PASS')
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                    self.screenShot(resultMessage)
                else:
                    self.resultList.append('FAIL')
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append('FAIL')
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)

        except:
            self.resultList.append("FAIL")
            self.log.error("### EXCEPTION OCCURRED !!!!")
            self.screenShot(resultMessage)

    def mark(self,result,resultMessage):
        """ Mark the result of the verification point in a test case"""
        self.setResult(result,resultMessage)

    def markFinal(self,testName,result,resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """

        self.setResult(result,resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert result == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert result == True
