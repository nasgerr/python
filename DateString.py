class DateString:
    def __init__(self, date_string):
        try:
            day, month, year = map(int, date_string.split('.'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 3000):
                raise DateError
            self.day = day
            self.month = month
            self.year = year
        except (ValueError, DateError):
            raise DateError("Неверный формат даты")

        def __str__(self):
            return f"{self.day:02d}.{self.month:02d}.{self.year:04d}"

class DateError(Exception):
    pass

date_string = input()

try:
    date = DateString(date_string)
    print(date)
except DateError:
    print("Неверный формат даты")

