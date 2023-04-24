from pages.cartPage import cartPageObject
from selenium.webdriver.common.by import By

class cartTasks:
    def __init__(self,driver):
        self.driver=driver
        self.listOfItems=self.driver.find_elements(By.XPATH,cartPageObject.itemsDiv)


    def getListOfItems(self):
        return self.listOfItems


    def assertListOfItems(self):
        i=0
        for item in self.getListOfItems():
            i=i+1
        return i