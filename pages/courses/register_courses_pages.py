import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    ''' Locators '''
    search_box = "//input[@id='search' and @placeholder='Search Course']"
    all_courses = "//a[@href='/courses' and contains(text(),'ALL COURSES')]"
    search_button = "//button[@type='submit']"
    required_course = "//div[@class='zen-course-thumbnail']"
    enroll_button = "//button[contains(text(),'Enroll in Course')]"
    #card_num = "//input[@aria-label='Credit or debit card number']"
    card_num = "//div[@id='card-number']"
    card_exp = "//input[@aria-label='Credit or debit card expiration date']"
    card_cvv = "//input[@aria-label='Credit or debit card CVC/CVV']"
    buy_button = "//button[@type='button' and contains(normalize-space(),'Buy')][1]"
    card_invalid_message = "//span[contains(text(),'Your card number is invalid')]"
    js_text = "//h2[contains(text(),'JavaScript')]"  #JavaScript for beginners


    def selectALlCourses(self):
        self.elementClick(locator=self.all_courses,locatorType='xpath')

    def enterCourseName(self,name):
        self.sendKeys(name,locator=self.search_box,locatorType='xpath')

    def enterSearchbuttonForCourse(self):
        self.elementClick(locator=self.search_button,locatorType='xpath')

    def selectCourse(self):
        self.elementClick(locator=self.required_course,locatorType='xpath')

    def clickonEnrollCourseButton(self):
        self.elementClick(locator=self.enroll_button, locatorType='xpath')

    def findTextonCourse(self):
        element_text = self.isElementPresent(locator=self.js_text,locatorType='xpath')
        return element_text

    def enterCardNum(self,num):
        #self.switchToIframe(xpath="//iframe[@name='__privateStripeFrame9353']")
        self.switchToIframe(name='__privateStripeFrame9353')
        self.sendKeys(num,locator=self.card_num,locatorType='xpath')
        self.switchToDefaultContent()

    def enterCardExp(self,exp):
        #self.switchToIframe(xpath="//iframe[@name='__privateStripeFrame9355']")
        self.switchToIframe(name='__privateStripeFrame9355')
        self.sendKeys(exp, locator=self.card_exp, locatorType='xpath')
        self.switchToDefaultContent()

    def enterCardCVV(self,cvv):
        #self.switchToIframe(xpath="//iframe[@name='__privateStripeFrame9354']")
        self.switchToIframe(name='__privateStripeFrame9354')
        self.sendKeys(cvv, locator=self.card_cvv, locatorType='xpath')
        self.switchToDefaultContent()

    def clearCardNum(self):
        self.clearNumItem(locator=self.card_num,locatorType='xpath')

    def enterCardNum(self,num):
        self.sendKeys(num,locator=self.card_num,locatorType='xpath')

    def clckBuyButton(self):
        self.elementClick(locator=self.buy_button,locatorType='xpath')


    def enterCreditCardInformation(self,num,exp,cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.clearCardNum()
        self.enterCardNum(num)

    def enrollCourse(self,num="",exp="",cvv=""):
        self.clickonEnrollCourseButton()
        self.webScroll(direction='down')
        time.sleep(2)
        self.enterCreditCardInformation(num,exp,cvv)
        self.clckBuyButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self.card_invalid_message,locatorType='xpath')

    def getTextonCourse(self):
        self.getText()














