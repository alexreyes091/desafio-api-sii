from SII.DateSII import DateSII
from SII.helpers.url import getURL

class UnidadFomento:
    'Clase que muestra la unidad de fomento en un momento dado (fecha)'

    # CONSTANTES
    MIN_DATE = DateSII(2013, 1, 1)

    def __init__(self, year: int = 0, month: int = 0, day: int = 0):
        self._date = DateSII(year, month, day)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, dateTuple: [int] = [2013, 12, 31] ):
        year, month, day = dateTuple
        self._date = DateSII(year, month, day)

    def isValidDate(self):
        'Retorna True si la fecha es válida, False en caso contrario.'
    
        # 1. Validamos la fecha minima
        if ( self._date.formatDate < self.MIN_DATE.formatDate): return False 

        #2. Validamos el formato de fecha
        return True
        
    def getUrlUF(self):
        'Retorna la UF de la fecha especificada'
        
        if not self.isValidDate(): return None

        year, month, day = self._date.formatDate
        url = getURL(year)
        
        return url
    