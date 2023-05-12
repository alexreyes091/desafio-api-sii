import requests
from SII.DateSII import DateSII
from bs4 import BeautifulSoup
from SII.helpers.months import getMonth

class ScrapingSII:
    '''Clase que permite obtener la UF de una fecha específica desde el sitio web del SII.''' 

    def __init__(self, url: str = ''):
        self._url = url
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url: str = ''):
        self._url = url
    
    def getDataScrap(self, date: DateSII):
        '''Retorna los datos de la fecha especificada o devuelve None si la fecha no es válida.'''
        
        URL = self.url
        month = getMonth(int(date.month))
        req = requests.get(URL)
        status_code = req.status_code
        print(month)

        if status_code == 200:
            html = BeautifulSoup(req.text, 'html.parser')
            div = html.find('div',  id='mes_enero')
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
        
        return None