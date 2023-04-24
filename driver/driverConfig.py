from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

#en este archivo se define el driver general y cómo se ejecutaran las pruebas

class Driver:
    def __init__(self):
        self.driver = None


    def set_driver(self):
        option = Options()
        #option.add_argument('--headless')
        option.add_argument('start-maximized')
        #self.driver = webdriver.Chrome(options=option, service=Service(GeckoDriverManager().install()))
        self.driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(30)
        return self.driver