import requests
from api.SII.models.DateSII import DateSII
from bs4 import BeautifulSoup
from api.SII.helpers.tagsTable import getTagOfTable

class ScrapingSII:
    '''Clase que permite obtener la UF de una fecha específica desde el sitio web del SII.''' 

    def __init__(self, url: str = ''):
        self._url = url
        self._allDataScrap = []
        self._dataScrapByDay = []
        
        # Diccionario de tipos de busqueda
        self.typeSearch = {
            'day',
            'month',
            'year',
        }
        
    # GETTERS & SETTERS
    #-------------------------------------------------------------------------------------------
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url: str = ''):
        self._url = url

    @property
    def allDataScrap(self):
        return self._allDataScrap

    @allDataScrap.setter
    def allDataScrap(self, data: [str]):
        self._allDataScrap = data

    @property
    def dataScrapByDay(self):
        return self._dataScrapByDay

    @dataScrapByDay.setter
    def dataScrapByDay(self, data: [str]):
        self._dataScrapByDay = data
    #-------------------------------------------------------------------------------------------

    # SORT FUNCTIONS
    #-------------------------------------------------------------------------------------------
    def getSortDataScrapByDay(self, data: [str]):
        '''Retorna una lista con los datos ordenados por día.'''
        try:
            data.sort(key = self.sortDataScrap)
            print('INFO: Registros ordenados correctamente.')
        except: 
            print('ALERT: No se lograron organizar los datos.')

        return data
        
    def sortDataScrap(self, key: str):
        '''Retorna el vlaor de la llave "day" de forma ordenada'''
        return key['day']
    #-------------------------------------------------------------------------------------------

    
    # MAIN FUNCTION
    #-------------------------------------------------------------------------------------------
    def getDataPerDay(self, req: str, month: str, day: int):
        dataScrap = []

        try:
            html = BeautifulSoup(req.text, 'html.parser')
            div = html.find('div',  id=month)
            table = div.find('table')
            rows = table.find_all('tr')
            for row in rows:
                columnsContent = row.find_all('td')
                columnsHeader = row.find_all('th')
                
                for data in zip(columnsHeader, columnsContent):
                    if(int(data[0].text) == int(day)):
                        dataScrap.append({'day': int(data[0].text),  'value': data[1].text})
                        print('INFO: Extraccion de datos completa.')
                        return dataScrap
                        
        except:
            print('ERROR: No se pudo extaer la data al tratar de hacer el scraping a la url designada.')

        return dataScrap


    def getDataPerMonth(self, req: str, month: str):
        dataScrap = []

        try:
            html = BeautifulSoup(req.text, 'html.parser')
            div = html.find('div',  id=month)
            table = div.find('table')
            rows = table.find_all('tr')
            for row in rows:
                columnsContent = row.find_all('td')
                columnsHeader = row.find_all('th')
                
                for data in zip(columnsHeader, columnsContent):
                    if(len(data[1].text) > 1):
                        dataScrap.append({'day': int(data[0].text),  'value': data[1].text})
            print('INFO: Extraccion de datos completa.')
        except:
            print('ERROR: No se pudo extaer la data al tratar de hacer el scraping a la url designada.')

        # Ordenamos los registros antes de enviarlo de regreso
        self.getSortDataScrapByDay(dataScrap)
        return dataScrap


    def getDataPerYear(self, req: str, year: str):
        dataScrap = {}
        try:
            html = BeautifulSoup(req.text, 'html.parser')
            div = html.find('div',  id=year)
            table = div.find('table')
            
            # Contenido del Header de la tabla de datos
            tableHeader = table.find_all('thead')
            header = tableHeader[0].find_all('th')


            # Contenido de la tabla de datos
            tableBody = table.find_all('tbody')
            # print(tableBody)
            indexMonth = 0
            for head in header[1:]:
                dataScrap[head.text] = []

                for body in tableBody:
                    for row in body.find_all('tr'):
                        columnsContent = row.find_all('td')
                        columnsHeader = row.find_all('th')

                        for col in columnsHeader:
                            valueContent = ''
                            if(columnsContent[indexMonth].text != '\xa0'):
                                value =columnsContent[indexMonth].text
                            else:
                                value = '0'

                            dataScrap[head.text].append({'day': int(col.text), 'value': value})
                indexMonth += 1

                    
            print('INFO: Extraccion de datos completa.')
        except:
            print('ERROR: No se pudo extaer la informacion al tratar de hacer el scraping a la url designada.')

        # Ordenamos los registros antes de enviarlo de regreso
        self.getSortDataScrapByDay(dataScrap)
        return dataScrap


    def saveDataScrap(self, date: DateSII, dataScrap: []):
        ''' Clase que almacena la estructura de la infromacion solicitada '''
    
        try:
            self.allDataScrap = {
                'year': date.year,
                'month': date.month,
                'days': dataScrap
            }
            print('INFO: Registro guardado correctamente.')
        except:
             print('ERROR: El registro no se guardado correctamente.')
        
        return 

    def saveDataScrapYear(self, date: DateSII, dataScrap: []):
        ''' Clase que almacena la estructura de la infromacion solicitada '''
    
        try:
            self.allDataScrap = {
                'year': date.year,
                'month': dataScrap
            }
            print('INFO: Registro guardado correctamente.')
        except:
             print('ERROR: El registro no se guardado correctamente.')
        
        return 


    def getScrap(self, date: DateSII, typeSearch: str = 'day'):
        '''Retorna datos de un dia en especifico o devuelve None si la fecha no es válida.'''
        
        try:
            # 1. Definimos previamente los valores requeridos.
            URL = self.url
            idTagDay = date.day
            idTagMonth = getTagOfTable(int(date.month))
            idTagYear = getTagOfTable(0)
            tempDataScrap = []

            # 2. Capturamos la rspuesta de la URL
            req = requests.get(URL)

            # 3. Si la URL es válida, entonces obtenemos los datos.
            if req.status_code == 200:
                
                match typeSearch:
                    case 'day':
                        tempDataScrap = self.getDataPerDay(req, idTagMonth, idTagDay)
                        self.saveDataScrap(date, tempDataScrap)

                    case 'month':
                        tempDataScrap = self.getDataPerMonth(req, idTagMonth)
                        self.saveDataScrap(date, tempDataScrap)

                    case 'year':
                        tempDataScrap = self.getDataPerYear(req, idTagYear)
                        self.saveDataScrapYear(date, tempDataScrap)
                    
                    case _:
                        print('ERROR: El tipo de busqueda no es valido.')
                        return

                return self.allDataScrap
            else:
                print ("Status Code %d" % status_code)
                return
            
        except:
            print('ERROR: Algo salio mal en la extraccion de datos.')
            return
    #-------------------------------------------------------------------------------------------