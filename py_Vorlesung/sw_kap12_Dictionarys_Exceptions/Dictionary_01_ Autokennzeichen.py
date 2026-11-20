# Ein Dictionary instanziieren
kreis = {"SL":"Schleswig", 
         "FL":"Flensburg",
         "HG":"Bad Homburg"}


# Abfrage des Schlüssels "FL" 
print(kreis["FL"])



kreis["BOH"] = "Bocholt"
kreis["HG"] = "Hochtaunuskreis"
del kreis["FL"]


# Vollständiges auslesen
for i in kreis:
    print(i, kreis[i])


if ("HG" in kreis):
    print("ja")


kreis.clear()

# Vollständiges ausgeben
for i in kreis:
    print(i, kreis[i])