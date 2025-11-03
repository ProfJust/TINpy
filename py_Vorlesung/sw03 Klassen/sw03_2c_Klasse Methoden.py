# [DOW25] Kapitel 15 Klassen und Methoden
from copy import copy

class Time:
    """Represents a time of day."""  # Docstring, der den Zweck der Klasse erklärt 
    def __init__(self, hour=0, minute=0, second=0):  # Konstruktor
        self.hour = hour
        self.minute = minute
        self.second = second
    
    #--- Eine Methode zur Ausgabe der Zeit ----
    def print_time(self):
        s = f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
        print(s)

    #--- Eine Funktion um ein Time()-Objekt mit Startwerten zu instanzieren
    def make_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        return self
    
    def get_time(self):
        return self.hour, self.minute, self.second

    def increment_time(self, hours, minutes, seconds):
        self.hour += hours
        self.minute += minutes
        self.second += seconds
        # Python bietet die eingebaute Funktion divmod(a, b), 
        # die das Tupel (a // b,  a % b) liefert, 
        # also ganzzahligen Quotienten und Rest in einem Aufruf.
        rest, self.second = divmod(self.second, 60)
        rest, self.minute = divmod(self.minute + rest, 60)
        rest, self.hour   = divmod(self.hour + rest , 60)

    def add_time(self, hours, minutes, seconds):
        self.increment_time(hours, minutes, seconds) # time wird nicht berändert
        return self

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    # def int_to_time(self, seconds):
    #     minute, second = divmod(seconds, 60)
    #     hour, minute = divmod(minute, 60)
    #     return self.make_time(hour, minute, second)  # Henne Ei Problem ??
    @staticmethod
    def int_to_time(seconds): # Statische Methode ohne self
        time_object = Time()
        minute, second = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)
        return time_object.make_time(hour, minute, second)
    
    def is_after(self, other):
        print(self)
        print(other)
        print("time, other", self.time_to_int(), other.time_to_int())
        return self.time_to_int() > other.time_to_int()
    
    def __str__(self):
        s = f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
        return s
    
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return Time.int_to_time(seconds)
    
    def is_valid(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        if not isinstance(self.hour, int):
            return False
        if not isinstance(self.minute, int):
            return False
        return True

#--------------------------------------------------------------------
if __name__ == '__main__':
    start = Time(9, 20, 0)    
    
    dauer = Time(-9, 20, -20)
    print(dauer.is_valid())
    ende = start + dauer

    einstring = str(ende)
    print("ende", einstring)