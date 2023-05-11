import requests
from bs4 import BeautifulSoup
from .env import URL

URL = 'https://www.sii.cl/valores_y_fechas/uf/uf2023.htm'

req = requests.get(URL)
status_code = req.status_code

if status_code == 200:
    html = BeautifulSoup(req.text, 'html.parser')
    div = html.find('div',  id='mes_all')
    table = div.find('table')
    rows = table.find_all('tr')
    for row in rows:
        columnsContent = row.find_all('td')
        columnsHeader = row.find_all('th')
        
        for data in zip(columnsHeader, columnsContent):
            if(len(data[1].text) > 1):
                print(data[0].text + ": " + data[1].text)

else:
    print ("Status Code %d" % status_code)