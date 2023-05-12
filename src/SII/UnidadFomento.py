from SII.DateSII import DateSII
from SII.helpers.url import getURL, statusRequest

class UnidadFomento:
    '''Clase que muestra la unidad de fomento en un momento dado (fecha) 
    y que permite obtener una URL con la unidad de fomento de una fecha específica'''

    def __init__(self, year: int = 0, month: int = 0, day: int = 0):
        self._date = DateSII(year, month, day)
        self._minDate = DateSII(2013, 1, 1)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, dateTuple: [int] = [2013, 12, 31] ):
        year, month, day = dateTuple
        self._date = DateSII(year, month, day)

    @property
    def minDate(self):
        return self._minDate

    @minDate.setter
    def minDate(self, dateTuple: [int] = [2013, 1, 1]):
        year, month, day = dateTuple
        self._minDate = DateSII(year, month, day)

    def isValidDate(self):
        'Retorna True si la fecha es válida, False en caso contrario.'
    
        # 1. Validamos la fecha minima
        if ( self._date.formatDate < self.minDate.formatDate): return False 

        #2. Validamos el formato de fecha
        return True
        

    def isValidUrl(self, url: str = ''):
        '''Retorna True si la URL es válida, False en caso contrario.'''
        return statusRequest(url) == 200


    def getUrl(self, type: str = 'uf'):
        '''Retorna la URL de la fecha especificada entre los tipos "uf", "dolar", o "utm",
        o devuelve None si la fecha no es válida.'''
        
        if not self.isValidDate(): return None

        year, month, day = self._date.formatDate
        url = getURL(year, type)
        
        return url
    