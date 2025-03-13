from datetime import datetime
 
class Person:
    def __init__(self, birthdate):
        self.birthdate = self._normalize_date(birthdate)
        self.today = datetime.today()
   