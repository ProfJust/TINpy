# [DOW25] Kapitel 14 Klassen und Funktionen

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
#--------------------------------------------------------------------
# In Python ist __name__ der Modulname; 
# beim direkten Ausführen eines Skripts ist er main,
# beim Import ist er der Modulname des Imports
#
#  Das “name-main-Idiom”  prüft, ob ein Modul als Hauptprogramm gestartet
#  wurde und führt dann den darauffolgenden Codeblock aus

if __name__ == '__main__':
    # Objekt der Klasse Time() anlegen (Instanzieren)
    lunch = make_time(11, 59, 1)  # Mit Parametern
  
    # Aufruf der Funktion
    print_time(lunch)
    
    
   

   