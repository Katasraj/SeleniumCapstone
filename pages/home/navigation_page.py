from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import utilities.custom_logger as cl
from base.basepage import BasePage
from configfiles.location_path import Path_Login
import time
from utilities.Path import PathFind

#p = PathFind().Locations()
class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.login_locator = Path_Login().login_element_location()
        self.locator_nav = Path_Login().navigation_elements()

    def navigateToALlCourses(self):
        self.elementClick(self.locator_nav['all_courses'],locatorType="xpath")
        #self.elementClick(locator=self.all_courses, locatorType="xpath")

    def navigateToPractice(self):
        self.elementClick(self.locator_nav['practice_dropdown_button'],locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.locator_nav['element_practice'],locatorType='xpath')
        # ElementClick = self.waitForElement(locator=self.element_practice,locatorType='xpath',pollFrequency=1)
        # self.elementClick(ElementClick)

    def clickSigninLink(self):
        # self.getSigninLink().click()
        self.elementClick(self.login_locator['signin_link'],locatorType='xpath')

    def enterEmail(self,email):
        #self.getEmailField().send_keys(email)
        self.sendKeys(email,self.login_locator['emialLogin'],locatorType='xpath')

    def enterPassword(self,password):
        #self.getPasswordField().send_keys(password)
        self.sendKeys(password,self.login_locator['password'],locatorType='xpath')

    def clickLoginButton(self):
        #self.getLoginButton().click()
        self.elementClick(self.login_locator['login_button'],locatorType='xpath')

    def login(self,email="",password=""):
        self.clickSigninLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self.login_locator['userIcon_After_login'],locatorType='xpath')
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self.login_locator['invalid_login'],locatorType='xpath')
        return result

    def clearItem(self,locator,locatorType="id"):
        item = self.getElement(locator,locatorType)
        if item:
            item.clear()
        else:
            self.log.info("Item not found to clear")

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Login")


