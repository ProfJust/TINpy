# ------------------------------------------------
# Version vom 16.10.2026 by OJ
# -------------------------------------------------
# WHS - Campus Bocholt - TINpy
# Grundprinzip: try und except
# -------------------------------------------------
a = 10
b = 0

try:
    ergebnis = a / b
    print(f"Ergebnis: {ergebnis}")

except ZeroDivisionError:
    print("Fehler: Division durch null!")

print("Programm läuft weiter...")

# ---------------------------------------------
try:
    zahl = int(input("Ganze Zahl eingeben: "))
    ergebnis = 100 / zahl
    print(f"Ergebnis: {ergebnis}")

except ValueError:
    print("Fehler: Keine gültige ganze Zahl!")

except ZeroDivisionError:
    print("Fehler: Division durch null!")


# ---------------------------------------------
try:
    zahl = int(input("Zahl eingeben: "))
    ergebnis = 100 / zahl

except ValueError:
    print("Ungültige Eingabe!")

except ZeroDivisionError:
    print("Division durch null!")

else:  # Wenn im try-Block keine Exception auftritt
    print(f"Ergebnis: {ergebnis}")

finally:  # Immer beim Verlassen der Anweisung, auch bei einem Fehler
    print("Berechnung abgeschlossen.")