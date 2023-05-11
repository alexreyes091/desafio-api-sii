
class UnidadFomento(self):
    'Clase que representa la unidad de fomento en un momento dado (fecha)'

    def __init__(self, date):
        self._date = date

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    def is_valid_date(self, date):
        return True
        

    
    
