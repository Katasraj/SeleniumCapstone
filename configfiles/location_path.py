class Path_Login:
    def login_element_location(self):
        locators_login = {}
        locators_login['signin_link'] = "//a[@href='/login' and text()='Sign In']"
        locators_login['emialLogin'] = "//input[@id='email' and @placeholder='Email Address']"
        locators_login['password'] = "//input[@id='login-password']"
        locators_login['login_button'] = "//button[@type='button' and @id = 'login']"
        locators_login['userIcon_After_login'] = "//button[@type='button' and @id='dropdownMenu1']"
        locators_login['invalid_login'] = "//span[contains(text(),'Incorrect login details')]"
        locators_login['user_icon_DropDown_button'] = "//a[@class='dynamic-link']//span[@class='caret']"
        locators_login['logout_loc'] = "//a[@href='/logout']"
        locators_login['my_courses'] = "//div[@class='col-md-12']//h1[contains(text(),'My Courses ')]"

        return locators_login

    def navigation_elements(self):
        locators_nav = {}
        locators_nav['practice_dropdown_button'] = "//div[@class='dropdown']//a[@type='button' and contains(text(),'PRACTICE')]//span[@class='caret']"
        locators_nav['element_practice'] = "//a[@href='/practice' and contains(text(),'Element Practice')]"
        locators_nav['all_courses'] = "//a[@href='/courses' and contains(text(),'ALL COURSES')]"

        return locators_nav

p = Path_Login()
print(type(p.navigation_elements()['all_courses']))
print(p.navigation_elements()['all_courses'])
# d = p.Locations()
# print(p)
# print(p['signin_link'])

