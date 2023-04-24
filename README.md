# testAutomation2023

*Framework diseñado con: Selenium, webdriver, webdriver-manager, python, unittest y htmlRunner (reportes)*

#### Para ejecutar se debe primero instalar el requirements.txt (ejecutando  "pip install -r requirements.txt")

*El proyecto está compuesto por distintas carpetas las cuales son:*
+ ApiTest la cual contiene el archivo con los tests por API.
+ Data la cual contiene por ejemplo el json para el test_login el cual está variabilizado y se maneja por data driven, y el archivo .txt de casos de prueba.
+ Driver es la carpeta en la que se encuentra la configuración del driver que se va a utilizar en los tests.
+ Pages en esta carpeta se encuentran los archivos en los que se localizan los ids/xpaths de los webElements a utilizar
+ Tasks en esta carpeta se encuentran los getters de los webElements y también el desarrollo de las funcionalidades para las que se utilizan dichos elementos.
+ Tests se encuentran los tests y la suite de pruebas
+ Utils se encuentran archivos generales que sirven para las pruebas
