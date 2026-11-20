
# Warenlager mit einem Dictionary

lager = {
    "Apfel": 25,
    "Banane": 18,
    "Orange": 30,
    "Birne": 12,
    "Kiwi": 8
}

# Aufgabe 1: Anzahl der Äpfel ausgeben
print("Anzahl Äpfel:", lager["Apfel"])


# Aufgabe 2: 5 Bananen verkaufen
lager["Banane"] -= 5
print("Anzahl Bananen:", lager["Banane"])


# Aufgabe 3: 20 Erdbeeren hinzufügen
lager["Erdbeere"] = 20


# Aufgabe 4: Kiwis entfernen
lager.pop("Kiwi")


# Aufgabe 5: Alle Produkte ausgeben
print("\nAktueller Warenbestand:")

for produkt, anzahl in lager.items():
    print(f"{produkt}: {anzahl} Stück")


# Aufgabe 6: Gesamtbestand berechnen
gesamt = sum(lager.values())

print("\nGesamtbestand:", gesamt, "Stück")


# Aufgabe 7: Produkt suchen
produkt = input("\nProdukt suchen: ")

if produkt in lager:
    print(f"{produkt}: {lager[produkt]} Stück")
else:
    print("Produkt nicht gefunden!")
