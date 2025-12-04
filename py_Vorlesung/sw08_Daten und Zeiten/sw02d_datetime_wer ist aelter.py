from datetime import datetime

# Eingabeformat festlegen, z.B. TT.MM.JJJJ
FORMAT = "%d.%m.%Y"

# Geburtsdaten einlesen
g1_str = input("Geburtsdatum Person 1 (TT.MM.JJJJ): ")
g2_str = input("Geburtsdatum Person 2 (TT.MM.JJJJ): ")

# Strings in datetime-Objekte umwandeln
geb1 = datetime.strptime(g1_str, FORMAT).date()
geb2 = datetime.strptime(g2_str, FORMAT).date()

print("Geburtsdatum Person 1:", geb1)
print("Geburtsdatum Person 2:", geb2)   
# Vergleichen
if geb1 < geb2:
    print("Person 1 ist älter.")
elif geb1 > geb2:
    print("Person 2 ist älter.")
else:
    print("Beide sind am selben Tag geboren.")
