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

        return locators_login

    def navigation_elements(self):
        locators_nav = {}
        locators_nav['practice_dropdown_button'] = "//div[@class='dropdown']//a[@type='button' and contains(text(),'PRACTICE')]//span[@class='caret']"
        locators_nav['element_practice'] = "//a[@href='/practice' and contains(text(),'Element Practice')]"
        locators_nav['all_courses'] = "//a[@href='/courses' and contains(text(),'ALL COURSES')]"

        return locators_nav

    def login_details(self):
        user_login_details = {}
        user_login_details['username'] = ["kotarinaga1@gmail.com"]
        user_login_details['password'] = ["Katasraj111#"]

        return user_login_details

    def single_user_login_details(self):
        single_user_user_login_details = {}
        single_user_user_login_details['username'] = "kotarinaga1@gmail.com"
        single_user_user_login_details['password'] = "Katasraj111#"
        return single_user_user_login_details

    def courses_location(self,courseName=None):
        courses_page = {}
        courses_page['all_courses'] = "//a[@href='/courses' and contains(text(),'ALL COURSES')]"
        courses_page['search_box'] = "//input[@id='search' and @placeholder='Search Course']"
        courses_page['search_button'] = "//button[@type='submit']"
        courses_page['required_course'] = "//div[@class='zen-course-thumbnail']"
        courses_page['enroll_button'] = "//button[contains(text(),'Enroll in Course')]"
        courses_page['course_text'] = "//h2[contains(text(),'JavaScript')]"
        courses_page['category'] = "//select[@name='categories']"
        courses_page['drop_down_course'] = f"//select[@name='categories']/..//option[contains(text(),'{courseName}')]"
        courses_page['course_category'] = f"//div[@class='col-md-5']//h1[contains(text(),'{courseName}')]"

        return courses_page




p = Path_Login()
print(p.courses_location())
# print(p.login_details()['username'])
# print(type(p.navigation_elements()['all_courses']))
# print(p.navigation_elements()['all_courses'])
# d = p.Locations()
# print(p)
# print(p['signin_link'])

#Selenium WebDriver 4 With Java,15