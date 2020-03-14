# nazwa pliku powinna być count_parking_free
from datetime import datetime
from math import ceil


class CountParkingFee:
    """Obliczanie stawki za postój"""

    def __init__(self, parking_peroid, yacht_lenght, yacht_width):
         # widzisz jak tutaj przesyłasz hasha, zamiast dwóch parametrów? 
        # A zobacz tutaj https://github.com/Adi52/Program_marine/blob/master/CreateDeclaration.py#L6 XD
        
         # jeżeli nie planujesz by te zmienne były publiczne i używane z zewnątrz, to daj im do nazwy podłogę
        self._parking_peroid = parking_peroid 
        self._yacht_length = yacht_lenght
        self._yacht_width = yacht_width
         # w CreateDeclaration.py zamiast .days używasz self.count_days()

        self.days = self.count_days()

    def count_days(self) -> Int:
        # Obliczenie ilości dni w okresie postoju
        date_format = "%d.%m.%Y"
        a = datetime.strptime(self.parking_peroid['from'], date_format)
        b = datetime.strptime(self.parking_peroid['to'], date_format)
        delta = b - a
        return delta.days

    def summer_fee(self) -> Int:
        # Jeżeli okres dłuższy niż 184 dni to przysługuje zniżka 30%
        if self.days >= 183:
            return ceil(self.yacht_length) * 4.30 * 184 * 0.7
        else:
            return ceil(self.yacht_length) * 4.30 * self.days

    def winter_fee(self) -> Int:
        # Opłata zima: długość * szerokość * 0.25 * (ilość dni - 184)
        return ceil(self.yacht_length) * ceil(self.yacht_width) * 0.25 * (self.days - 184)

    def parking_fee(self) -> Int:
        if self.days in [364, 365, 366]:
            return round(self.summer_fee() + self.winter_fee(), 2)
        else:
            return round(self.summer_fee(), 2)
