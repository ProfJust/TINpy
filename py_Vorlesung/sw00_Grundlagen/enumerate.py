# Beispiel enumerate(liste)
# ------------------------------

drehzahl = [1000, 1200, 1400, 1600]
for wert in drehzahl:
    print(wert)  # Ausgabe der Listenwerte

for index, wert in enumerate(drehzahl):
    print(index, wert)   # Ausgabe der Listenwerte mit Index

# das ist nützlich wenn man andere Indizes ansprechen möchte
for i, wert in enumerate(drehzahl):
    if i >= 2:  # Index i-2 muss vorhanden sein!
        mittelwert = (
            drehzahl[i-2]    # vorletzter vergangener Wert
            + drehzahl[i-1]  # letzter    vergangener Wert
            + drehzahl[i]
        ) / 3
        print("Avg: ", mittelwert)

# for i, wert in enumerate(drehzahl, start=2):   # (liste, startindex)
#     print(i, wert)   # Ausgabe der Listenwerte mit Index
