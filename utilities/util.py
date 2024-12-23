import time
import traceback
import random,string
import utilities.custom_logger as cl
import logging

class Util(object):
    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        ''''Put the program to wait for a specified amount of time'''

        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type='letters'):

        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self,charCount=10):
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        nameList = []
        for i in range(0,listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyTextContains(self,actualText,expectedText):
        self.log.info("Actual From Application Web UI --> :: " + actualText)
        self.log.info("Expected From Application Web UI --> :: " + actualText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self,actualText,expectedText):
        pass


