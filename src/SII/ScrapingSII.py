import requests
from SII.DateSII import DateSII
from bs4 import BeautifulSoup
from SII.helpers.months import getMonth

class ScrapingSII:
    '''Clase que permite obtener la UF de una fecha específica desde el sitio web del SII.''' 

    def __init__(self, url: str = ''):
        self._url = url
        self._allDataScrap = []
        self._dataScrapByDay = []
        
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
    
    # MAIN FUNCTION
    #-------------------------------------------------------------------------------------------
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


    def sortDataScrap(self, key: str):
        '''Retorna el vlaor de la llave "day" de forma ordenada'''
        return key['day']
        

    def getSortDataScrapByDay(self, data: [str]):
        '''Retorna una lista con los datos ordenados por día.'''
        try:
            data.sort(key = self.sortDataScrap)
            print('INFO: Registros ordenados correctamente.')
        except: 
            print('ALERT: No se lograron organizar los datos.')

        return data


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


    def getScrap(self, date: DateSII, typeSearch: str = 'day'):
        '''Retorna datos de un dia en especifico o devuelve None si la fecha no es válida.'''
        
        try:
            # 1. Definimos previamente los valores requeridos.
            URL = self.url
            month = getMonth(int(date.month))
            day = date.day
            tempDataScrap = []

            # 2. Capturamos la rspuesta de la URL
            req = requests.get(URL)

            # 3. Si la URL es válida, entonces obtenemos los datos.
            if req.status_code == 200:
                
                match typeSearch:
                    case 'day':
                        tempDataScrap = self.getDataPerDay(req, month, day)

                    case 'month':
                        tempDataScrap = self.getDataPerMonth(req, month)
                    
                    case _:
                        return

                # 4. Guardamos la informacion
                self.saveDataScrap(date, tempDataScrap)

                return self.allDataScrap
            else:
                print ("Status Code %d" % status_code)
                return None
            
        except:
            print('ERROR: Algo salio mal en la extraccion de datos.')
            return


    def getAllDataScrap(self, date: DateSII):
        '''Retorna todos los datos de un mes en especifico o devuelve None si la fecha no es válida.'''
        
        try:
            # 1. Definimos previamente los valores requeridos.
            URL = self.url
            month = getMonth(int(date.month))
            # day = date.day
            tempAllDataScrap = []

            # 2. Capturamos la rspuesta de la URL
            req = requests.get(URL)

            # 3. Si la URL es válida, entonces obtenemos los datos.
            if req.status_code == 200:
                html = BeautifulSoup(req.text, 'html.parser')
                div = html.find('div',  id=month)
                table = div.find('table')
                rows = table.find_all('tr')
                for row in rows:
                    columnsContent = row.find_all('td')
                    columnsHeader = row.find_all('th')
                    
                    for data in zip(columnsHeader, columnsContent):
                        if(len(data[1].text) > 1):
                            tempAllDataScrap.append({'day': int(data[0].text),  'value': data[1].text})

                # 4. Organizamos la informacion y guardamos
                self.getSortDataScrapByDay(tempAllDataScrap)
                self.saveDataScrap(date, tempAllDataScrap)

                return self.allDataScrap
            else:
                print ("Status Code %d" % status_code)
                return None
            
        except:
            print('ERROR: No se pudo extaer la data al tratar de hacer el scraping a la url designada.')
            return

    #-------------------------------------------------------------------------------------------