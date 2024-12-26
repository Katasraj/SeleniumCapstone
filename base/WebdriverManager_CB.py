from sys import executable

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername = "chrome"

if browsername == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browsername == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browsername == "safari":
    driver = webdriver.Safari()
else:
    print(f"Please pass the correct browser: {browsername}")
    driver = None  # Set driver to None if no valid browser is selected

if driver:
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.letskodeit.com/")
    driver.quit()  # Fixed the typo from diver.quit() to driver.quit()
else:
    print("Driver was not initialized due to an incorrect browser name.")
