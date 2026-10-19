# ------------------------------------------------
# Version vom 16.10.2026 by OJ
# -------------------------------------------------
# WHS - Campus Bocholt - TINpy
# Grundprinzip: try und except
# -------------------------------------------------
def pruefe_abstand(abstand):
    if abstand < 0: 
        # Eigene Exceptions auslösen mit raise
        raise ValueError("Abstand darf nicht negativ sein!")
    return abstand


try:
    messwert = -15
    abstand = pruefe_abstand(messwert)
    print(f"Abstand: {abstand} cm")

except ValueError as fehler:
    print(f"Sensorfehler: {fehler}")

# ---------------------------------------

try:
    ergebnis = 10 / 0

except (ValueError, TypeError) as fehler:
    print(f"Ungültiger Wert: {fehler}")


# except:
#    print("Irgendein Fehler ist aufgetreten")