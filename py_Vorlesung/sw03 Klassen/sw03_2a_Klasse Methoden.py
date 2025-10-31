# [DOW25] Kapitel 15 Klassen und Methoden
from copy import copy

class Time:
    """Represents a time of day."""  # Docstring, der den Zweck der Klasse erklärt
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

    def int_to_time(self, seconds):
        minute, second = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)
        return self.make_time(hour, minute, second)  # Henne Ei Problem ??
    
#--------------------------------------------------------------------
if __name__ == '__main__':
    start = Time()
    start.make_time(9, 20, 0)
    
   # end = start.add_time(1, 32, 0)  # kein eigenes Objekt
   # print("start", end=" ");  Time.print_time(start)
   # print("end  ", end=" ");  Time.print_time(end)
        
    end_obj = Time()
    # falsch => end_obj = start
    # unschön aber funktioniert end_obj.make_time(9, 20, 0)
    h, m, s = start.get_time()
    end_obj.make_time(h, m, s)
    
    end_obj.add_time(1, 32, 0)
    print("start", end=" ");  Time.print_time(start)
    print("end  ", end=" ");  Time.print_time(end_obj)
    

    sekunden = start.time_to_int()
    print(" Sekunden seit 0:0:0 Uhr",sekunden )
    start.int_to_time(sekunden)
    start.print_time()
    
   

   