from pages.itemPage import itemPageObject
from selenium.webdriver.common.by import By

class itemTasks:
    def __init__(self,driver):
        self.driver=driver
        self.addItemBtn=self.driver.find_element(By.XPATH,itemPageObject.itemsAddBtn)


    def addCartItem(self):
        return self.addItemBtn.click()
