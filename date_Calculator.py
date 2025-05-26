class DateCalculator:
    def __init__(self, year, month, day):  # <-- Fix: double underscores

        self.original_year = year
        self.original_month = month
        self.day = day

        if month == 1 or month == 2:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

    def calculate_day_of_week(self):

        K = self.year % 100
        J = self.year // 100
        q = self.day
        m = self.month
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

# Test
date = DateCalculator(1589, 8, 15)
print("The day was:", date.calculate_day_of_week())
