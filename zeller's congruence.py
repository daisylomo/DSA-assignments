class DateCalculator:
    def __init__(self, year, month, day):
        # Store original date
        self.original_year = year
        self.original_month = month
        self.day = day

        # Adjust for Zeller's formula: Jan & Feb are 13 & 14 of the previous year
        if month < 3:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

        self.K = self.year % 100        # Year within the century
        self.J = self.year // 100       # Zero-based century

    def calculate_day_of_week(self):
        q = self.day
        m = self.month
        K = self.K
        J = self.J

        # Zeller's formula
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7

        # Map result to weekday name
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

    def __str__(self):
        day_of_week = self.calculate_day_of_week()
        return f"{self.original_year}-{self.original_month:02d}-{self.day:02d} was a {day_of_week}"


# 🎯 Example: What day of the week was September 15, 1589?
calc = DateCalculator(1589, 9, 15)
print(calc)
