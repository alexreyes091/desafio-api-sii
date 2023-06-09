from datetime import datetime

class DateSII:
    'Clase para representar fechas en formato YYYY-MM-DD'

    def __init__(self, year=2013, month=1, day=1):
        self._year = 0
        self._month = 0
        self._day = 0
        self.year = year
        self.month = month
        self.day = day

    # GETTERS & SETTERS
    #-------------------------------------------------------------------------------------------
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
            self._year = value
    
    @property
    def month(self):
        return self._month
    
    @month.setter
    def month(self, value):
        if self._is_valid_month(value):
            self._month = value
    
    @property
    def day(self):
        return self._day
    
    @day.setter
    def day(self, value):
        if self._is_valid_day(value):
            self._day = value
   
    @property
    def formatDate(self):
        return [self.year, self.month, self.day]

    #-------------------------------------------------------------------------------------------
    
    
    # VALIDACIONES GENERALES
    #-------------------------------------------------------------------------------------------
    def isValidDate(self, date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except:
            return False
    
    def _is_valid_month(self, month):
        return 0 <= month <= 12
    
    def _is_valid_day(self, day):
        return 0 <= day <= 31
    #-------------------------------------------------------------------------------------------