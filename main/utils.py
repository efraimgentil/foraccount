from datetime import date


class Date:
    
    YEARS = ((str(x), x) for x in range(2013 , date.today().year + 1 ))
    MONTHS = ((str(x), x) for x in range( 1 , 13  ))
    
    @staticmethod
    def years_available():
        return Date.YEARS
        
    @staticmethod
    def months_available():        
        return Date.MONTHS