from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import utilities.custom_logger as cl
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage
from configfiles.location_path import Path_Login
import time


#p = PathFind().Locations()
class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.locator = Path_Login.login_element_location(self)

    def clickSigninLink(self):
        self.elementClick(self.locator['signin_link'],locatorType='xpath')

    def enterEmail(self,email):
        self.sendKeys(email,self.locator['emialLogin'],locatorType='xpath')

    def enterPassword(self,password):
        self.sendKeys(password,self.locator['password'],locatorType='xpath')

    def clickLoginButton(self):
        self.elementClick(self.locator['login_button'],locatorType='xpath')

    def login(self,email="",password=""):
        self.clickSigninLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self.locator['userIcon_After_login'],locatorType='xpath')
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self.locator['invalid_login'],locatorType='xpath')
        return result

    def clearItem(self,locator,locatorType="id"):
        item = self.getElement(locator,locatorType)
        if item:
            item.clear()
        else:
            self.log.info("Item not found to clear")

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Login")


    def logout(self):
        # logoutLinkElement = self.waitForElement(self.user_icon_dropdown, locatorType='xpath', pollFrequency=1)
        # print("user_icon_dropdown **********", logoutLinkElement)
        self.elementClick(self.locator['user_icon_DropDown_button'],locatorType='xpath')
        self.elementClick(self.locator['logout_loc'],locatorType='xpath')





