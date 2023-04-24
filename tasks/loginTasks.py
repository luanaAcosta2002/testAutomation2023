from pages.loginPage import loginPageObject
from selenium.webdriver.common.by import By
class loginTasks:
    def __init__(self,driver):
        self.driver=driver
        self.user=self.driver.find_element(By.ID, loginPageObject.username)
        self.password= self.driver.find_element(By.ID, loginPageObject.password)
        self.loginBtn= self.driver.find_element(By.ID, loginPageObject.loginBtn)

    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password

    def getLogButton(self):
        return self.loginBtn

    def funcionLogin(self, user,password):
        self.getUser().send_keys(user)
        self.getPassword().send_keys(password)
        self.getLogButton().click()

    def getAssertInicio(self):
        return self.driver.find_element(By.XPATH, loginPageObject.assertTitleMain).is_displayed()