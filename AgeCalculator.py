from datetime import datetime
 
class Person:
    def __init__(self, birthdate):
        self.birthdate = self._normalize_date(birthdate)
        self.today = datetime.today()
    
    def _normalize_date(self, date_str):
        """Normalize date format to YYYY-MM-DD"""
        date_str = date_str.strip().replace("/", "-").replace(".", "-")
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format! Please use YYYY-MM-DD, YYYY/MM/DD, or YYYY.MM.DD.")
