import time

# aktuelles Datum ausgeben
jetzt = time.localtime()  # struct_time
heute_str = time.strftime("%Y-%m-%d", jetzt)
print("Heutiges Datum:", heute_str)

# N vom Benutzer einlesen
n = int(input("Gib die Anzahl der Tage N ein: "))

# N Tage in Sekunden (vereinfachend 24h pro Tag)
sek_pro_tag = 24 * 60 * 60
zukuenftig = time.localtime(time.time() + n * sek_pro_tag)

zukuenftig_str = time.strftime("%Y-%m-%d", zukuenftig)
print(f"Datum in {n} Tagen:", zukuenftig_str)
