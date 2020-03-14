from datetime import datetime
from math import ceil


class CountParkingFee:
    """Obliczanie stawki za postój"""

    def __init__(self, parking_peroid, yacht_lenght, yacht_width):
        self.parking_peroid = parking_peroid
        self.yacht_length = yacht_lenght
        self.yacht_width = yacht_width
        self.days = self.count_days()

    def count_days(self):
        # Obliczenie ilości dni w okresie postoju
        date_format = "%d.%m.%Y"
        a = datetime.strptime(self.parking_peroid['from'], date_format)
        b = datetime.strptime(self.parking_peroid['to'], date_format)
        delta = b - a
        return delta.days

    def summer_fee(self):
        # Jeżeli okres dłuższy niż 184 dni to przysługuje zniżka 30%
        if self.days >= 183:
            return ceil(self.yacht_length) * 4.30 * 184 * 0.7
        else:
            return ceil(self.yacht_length) * 4.30 * self.days

    def winter_fee(self):
        # Opłata zima: długość * szerokość * 0.25 * (ilość dni - 184)
        return ceil(self.yacht_length) * ceil(self.yacht_width) * 0.25 * (self.days - 184)

    def parking_fee(self):
        if self.days in [364, 365, 366]:
            return round(self.summer_fee() + self.winter_fee(), 2)
        else:
            return round(self.summer_fee(), 2)
