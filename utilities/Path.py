class PathFind:

    def Locations(self):

        locators = {}
        locators['signin'] = "//a[@href='/login' and text()='Sign In']"
        locators['emialLogin'] = "//input[@id='email' and @placeholder='Email Address']"
        locators['password'] = "//input[@id='login-password']"
        locators['login_button'] = "//button[@type='button' and @id = 'login']"
        locators['userIcon'] = "//button[@type='button' and @id='dropdownMenu1']"

        return locators

p = PathFind().Locations()
# d = p.Locations()
print(p)
print(p['signin'])







