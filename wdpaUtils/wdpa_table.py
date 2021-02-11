from datetime import datetime, date

class ProtectedAreas:
    def __init__(self):
        
        self.created_date = self.getDate()

    
    def getDate(date_format= '%Y-%m-%d %H:%M:%S'): 
        pa_date = datetime.now()
        return date.strftime(pa_date, '%Y-%m-%d %H:%M:%S')
