# ============================================================
# Python-Grundlagen – Übungsskript für die Konsole
# ============================================================

print("=== Python Grundlagen ===")

# ------------------------------------------------------------
# 1. Eingabe und Ausgabe
# ------------------------------------------------------------

name = input("Wie heißen Sie? ")
print(f"Hallo {name}!")

# ------------------------------------------------------------
# 2. Zahlen und Datentypen
# ------------------------------------------------------------

alter = int(input("Wie alt sind Sie? "))
groesse = float(input("Wie groß sind Sie in Metern? "))

print(f"Alter: {alter}")
print(f"Datentyp Alter: {type(alter)}")

print(f"Größe: {groesse} m")
print(f"Datentyp Größe: {type(groesse)}")

# ------------------------------------------------------------
# 3. Rechnen mit Operatoren
# ------------------------------------------------------------

zahl1 = float(input("Erste Zahl eingeben: "))
zahl2 = float(input("Zweite Zahl eingeben: "))

print(f"Addition:       {zahl1 + zahl2}")
print(f"Subtraktion:    {zahl1 - zahl2}")
print(f"Multiplikation: {zahl1 * zahl2}")

if zahl2 != 0:
    print(f"Division:       {zahl1 / zahl2}")
else:
    print("Division durch 0 ist nicht erlaubt.")

# ------------------------------------------------------------
# 4. Boolesche Werte und Vergleiche
# ------------------------------------------------------------

print(f"zahl1 > zahl2:  {zahl1 > zahl2}")
print(f"zahl1 == zahl2: {zahl1 == zahl2}")
print(f"zahl1 != zahl2: {zahl1 != zahl2}")

# ------------------------------------------------------------
# 5. EVA-Beispiel: Roboter mit Abstandssensor
# ------------------------------------------------------------

print("\n=== Roboter-Abstandssensor ===")

abstand = float(input("Abstand zum Hindernis in cm: "))

if abstand < 20:
    print("STOPP! Hindernis zu nah.")

elif abstand < 50:
    print("Roboter fährt langsam.")

else:
    print("Roboter fährt normal weiter.")

# ------------------------------------------------------------
# 6. Logische Operatoren
# ------------------------------------------------------------

sensor_ok = True

if sensor_ok and abstand < 20:
    print("Sensor funktioniert und Hindernis wurde erkannt.")

if not sensor_ok:
    print("Fehler: Abstandssensor funktioniert nicht.")

# ------------------------------------------------------------
# 7. Strings
# ------------------------------------------------------------

roboter_name = input("Wie soll der Roboter heißen? ")

status = "bereit"

print(f"Roboter: {roboter_name}")
print(f"Status: {status}")

# ------------------------------------------------------------
# Ende
# ------------------------------------------------------------

print("\n=== Programm beendet ===")
