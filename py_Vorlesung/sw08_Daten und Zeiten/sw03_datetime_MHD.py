import time
from datetime import date, timedelta

# aktuelles Datum ausgeben
heute = date.today()
print("Heutiges Datum:", heute)

# N vom Benutzer einlesen
n = int(input("Gib die Anzahl der Tage N ein: "))

# Datum in N Tagen berechnen
zukuenftiges_datum = heute + timedelta(days=n)
print(f"Datum in {n} Tagen:", zukuenftiges_datum)

# kleine Pause, damit man die Ausgabe sehen kann (optional)
time.sleep(2)
