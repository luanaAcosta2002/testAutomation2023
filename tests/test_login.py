import unittest
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from driver.driverConfig import Driver
from tasks.loginTasks import loginTasks
import time
from ddt import ddt, file_data
from utils.html_test_runner import HTMLTestRunner

path=Path.cwd()
pathLogin=Path(path.parents[0],"data","loginTestsData.json")
@ddt
class loginSauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().set_driver()
        self.driver.get('https://www.saucedemo.com/')
        self.logFunction=loginTasks(self.driver)

    @file_data(pathLogin)
    def test_login(self,username, password, errorImgName):
        self.logFunction.funcionLogin(username,password)
        time.sleep(3)
        if EC.url_contains('/inventory.html')==True:
            self.assertTrue(self.logFunction.getAssertInicio())
            print("Finalizado")
        else:
            self.driver.save_screenshot(errorImgName)
            pass

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

    if __name__ =='__main__':
        unittest.main()