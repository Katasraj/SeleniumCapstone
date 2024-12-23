from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super(BasePage,self).__init__(driver) # need to verify why can't super(self,BasePage)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self,titleToVerify):
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle,titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

