import unittest
from driver.driverConfig import Driver
from tasks.loginTasks import loginTasks
import time
from tasks.cartTasks import cartTasks
from tasks.mainPageTasks import mainPageTasks
from tasks.itemTasks import itemTasks

class agregarAlCarrito(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().set_driver()
        self.driver.get('https://www.saucedemo.com/')
        self.logFunction=loginTasks(self.driver)

    def test_todosLosItems(self):
        self.logFunction.funcionLogin("standard_user","secret_sauce")
        self.assertTrue(self.logFunction.getAssertInicio())
        time.sleep(3)
        self.mainPage=mainPageTasks(self.driver)
        self.mainPage.seleccionarLosSeisItems()
        self.mainPage.carrito()
        time.sleep(3)
        self.itemsLista=cartTasks(self.driver)
        self.assertEqual(self.itemsLista.assertListOfItems(),6)

    def test_elementoPagIndividual(self):
        self.logFunction.funcionLogin("standard_user", "secret_sauce")
        self.assertTrue(self.logFunction.getAssertInicio())
        time.sleep(3)
        self.mainPage = mainPageTasks(self.driver)
        self.mainPage.elegirProducto("Sauce Labs Fleece Jacket")
        time.sleep(3)
        self.itemSolo=itemTasks(self.driver)
        self.itemSolo.addCartItem()
        self.mainPage.carrito()
        time.sleep(3)
        self.itemsLista = cartTasks(self.driver)
        self.assertEqual(self.itemsLista.assertListOfItems(), 1)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()