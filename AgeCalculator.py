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

    def calculate_age(self):
        """Calculate years, months, and days"""
        if self.birthdate > self.today:
            return "Error: Birthdate cannot be in the future!"

        years = self.today.year - self.birthdate.year
        months = self.today.month - self.birthdate.month
        days = self.today.day - self.birthdate.day

        if days < 0:
            months -= 1
            prev_month = self.today.month - 1 if self.today.month > 1 else 12
            prev_year = self.today.year if self.today.month > 1 else self.today.year - 1
            days += (datetime(prev_year, prev_month + 1, 1) - datetime(prev_year, prev_month, 1)).days

        if months < 0:
            years -= 1
            months += 12

        return f"Your age is {years} years, {months} months, and {days} days."

    def calculate_total_days(self):
        """Calculate total days lived"""
        total_days = (self.today - self.birthdate).days
        return f"You have lived for {total_days} days."
