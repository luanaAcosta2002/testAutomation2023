import requests
import json
import pprint

BASE_URL = 'https://www.mercadolibre.com.ar/menu/departments'
response = requests.get(BASE_URL)
result = json.loads(response.text)
pprint.pprint(result)
#print(result['name'][0])
for item in result:
    print("{0} : {1}".format(item, result[item]))

'no finalizado, no entendí del todo la consigna y presenté unos errores al comprender el json que arroja el response'''