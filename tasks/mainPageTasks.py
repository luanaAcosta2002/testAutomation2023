from pages.mainPage import mainPageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class mainPageTasks:
    def __init__(self,driver):
        self.driver=driver
        self.item1=self.driver.find_element(By.ID, mainPageObject.item1AddtoCart)
        self.item2 = self.driver.find_element(By.ID, mainPageObject.item2AddtoCart)
        self.item3 = self.driver.find_element(By.ID, mainPageObject.item3AddtoCart)
        self.item4 = self.driver.find_element(By.ID, mainPageObject.item4AddtoCart)
        self.item5 = self.driver.find_element(By.ID, mainPageObject.item5AddtoCart)
        self.item6 = self.driver.find_element(By.ID, mainPageObject.item6AddtoCart)

    def getItem1(self):
        return self.item1
    def getItem2(self):
        return self.item2
    def getItem3(self):
        return self.item3
    def getItem4(self):
        return self.item4
    def getItem5(self):
        return self.item5
    def getItem6(self):
        return self.item6

    def seleccionarLosSeisItems(self):
        self.getItem1().click()
        self.getItem2().click()
        self.getItem3().click()
        self.getItem4().click()
        self.getItem5().click()
        self.getItem6().click()

    def carrito(self):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, mainPageObject.cartSection)))
        return self.driver.find_element(By.ID,mainPageObject.cartSection).click()

    def elegirProducto(self, nombre):
        prod=self.driver.find_element(By.XPATH, f"//div[contains(text(),'{nombre}')]")
        prod.click()