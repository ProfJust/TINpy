
# Beispiel enumerate(liste)
# ------------------------------
drehzahl = [1000, 1200, 1400, 1600]
for wert in drehzahl:
    print(wert)  # Ausgabe der Listenwerte

for index, wert in enumerate(drehzahl):
    print(index, wert)  # Ausgabe der Listenwerte mit Index

# das ist nützlich wenn man andere Indizes ansprechen möchte
for i, wert in enumerate(drehzahl):
    if i >= 1 and i < len(drehzahl) - 1:  # Index muss vorhanden sein!
        mittelwert = (
            drehzahl[i-1]
            + drehzahl[i]
            + drehzahl[i+1]
        ) / 3
        print("Avg: ", mittelwert)
