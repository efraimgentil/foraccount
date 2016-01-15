from datetime import date

class DateUtil:
    
    YEARS = range(2013 , date.today().year + 1 ) 
    #((str(x), x) for x in range(2013 , date.today().year + 1 ))
    MONTHS = range( 1 , 13  )
    #((str(x), x) for x in range( 1 , 13  ))
    
    @staticmethod
    def years_available():
        return DateUtil.YEARS
        
    @staticmethod
    def months_available():        
        return DateUtil.MONTHS


from django.contrib.auth.models import User

class UserUtil:
    
    @staticmethod
    def get_current_user():
        return User.objects.get(pk = 2) 
        