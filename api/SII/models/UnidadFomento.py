from api.SII.models.DateSII import DateSII
from api.SII.helpers.url import getURL, statusRequest, unitTypes

class UnidadFomento:
    '''Clase que muestra la unidad de fomento en un momento dado (fecha) 
    y que permite obtener una URL con la unidad de fomento de una fecha específica'''

    def __init__(self, year: int = 0, month: int = 0, day: int = 0):
        self._date = DateSII(year, month, day)
        self._minDate = DateSII(2013, 1, 1)

    # GETTERS & SETTERS
    #-------------------------------------------------------------------------------------------
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
    #-------------------------------------------------------------------------------------------


    # VALIDACIONES GENERALES
    #-------------------------------------------------------------------------------------------
    def isValidDate(self):
        'Retorna True si la fecha es válida, False en caso contrario.'
        # 1. Validamos la fecha minima
        if ( self._date.formatDate < self.minDate.formatDate): return False 
        #2. Validamos el formato de fecha
        return True
        

    def isValidUrl(self, url: str = ''):
        '''Retorna True si la URL es válida, False en caso contrario.'''
        return statusRequest(url) == 200
    #-------------------------------------------------------------------------------------------


    # MAIN FUNCTION
    #-------------------------------------------------------------------------------------------
    def getUrl(self, unitType: unitTypes = 'uf'):
        '''Retorna la URL de la fecha especificada entre los tipos "uf", "dolar".
        Devuelve "Status Code 404" si la fecha no es válida.'''
        
        if not self.isValidDate(): 
            print(f"ERROR: La fecha ingresada debe de ser mayor a la fecha minima definida: ", self.minDate.formatDate)
            return

        year, month, day = self._date.formatDate
        url = getURL(year, unitType)
        
        return url
    #-------------------------------------------------------------------------------------------
