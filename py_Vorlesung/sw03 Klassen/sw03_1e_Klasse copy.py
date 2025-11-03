# [DOW25] Kapitel 14 Klassen und Funktionen
from copy import copy

class Time:
    """Represents a time of day."""  # Docstring, der den Zweck der Klasse erklärt


#--- Eine Funktion zur Ausgabe der Zeit ----
def print_time(time):
    s = f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}'
    print(s)

#--- Eine Funktion um ein Time()-Objekt mit Startwerten zu instanzieren
def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

#--- Eine Funktion die ein Time()-Objekt inkrementiert
def increment_time(time, hours, minutes, seconds):
    time.hour += hours
    time.minute += minutes
    time.second += seconds
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def increment_time2(time, hours, minutes, seconds):
    time.hour += hours
    time.minute += minutes
    time.second += seconds
    # Python bietet die eingebaute Funktion divmod(a, b), 
    # die das Tupel (a // b,  a % b) liefert, 
    # also ganzzahligen Quotienten und Rest in einem Aufruf.
    rest, time.second = divmod(time.second, 60)
    rest, time.minute = divmod(time.minute + rest, 60)
    rest, time.hour   = divmod(time.hour + rest , 24)

def add_time(time, hours, minutes, seconds):
    total = copy(time) # Kopie von time anfertigen
    increment_time2(total, hours, minutes, seconds) # time wird nicht berändert
    return total
#--------------------------------------------------------------------
# In Python ist __name__ der Modulname; 
# beim direkten Ausführen eines Skripts ist er main,
# beim Import ist er der Modulname des Imports
#
#  Das “name-main-Idiom”  prüft, ob ein Modul als Hauptprogramm gestartet
#  wurde und führt dann den darauffolgenden Codeblock aus

if __name__ == '__main__':
    start = make_time(9, 20, 0)
    end = add_time(start, 1, 32, 0)
    print_time(end)

    end2 = add_time(start, 24, 52, 0)
    print_time(end2)
    
   

   