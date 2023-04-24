import unittest
from utils.html_test_runner import HTMLTestRunner
from tests.test_login import loginSauceDemo
from tests.test_agregarAlCarrito import agregarAlCarrito

test1=unittest.TestLoader().loadTestsFromTestCase(loginSauceDemo)
test2=unittest.TestLoader().loadTestsFromTestCase(agregarAlCarrito)
testSuite=unittest.TestSuite([test1,test2])

outFile=open("ReportePrueba.html","w")
runner= HTMLTestRunner(stream=outFile, title='Test Report', description='Acceptance Tests')
runner.run(testSuite)