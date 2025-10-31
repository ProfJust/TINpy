# ue01_bmi.py
# -------------------------------
# TINpy - OJ 13.10.25
# ------------------------------
# Berechnet den Body Max Index
# -------------------------------

BMI_MIN = 18.5  # Konstante in GROSSBUCHSTABEN
BMI_MAX = 25.0  # maximale BMI (siehe Tabelle)


def eingabe():
    # ---------- Eingabe ----------------
    _masse_kg = float(input(" Geben Sie Ihr Gewicht in kg ein >"))
    print("Gewicht: ", _masse_kg)

    _groesse_m = float(input(" Geben Sie Ihre Größe in m ein >"))
    print("Groesse: ", _groesse_m)

    _alter_y = int(input(" Geben Sie Ihr Alter in Jahren ein >"))
    print("Alter: ", _alter_y)

    return _masse_kg, _groesse_m, _alter_y


def verarbeitung(_masse_kg, _groesse_m, _alter_y):
    # -----------Verarbeitung ----------
    _bmi = _masse_kg / (_groesse_m * _groesse_m)
    
    if _alter_y < 19:
        print(" Bewertung für <19 Jahre nicht möglich")
    elif _alter_y <= 24:
        BMI_MIN = 19.0
        BMI_MAX = 24.0
    elif _alter_y <= 34:
        BMI_MIN = 20.0
        BMI_MAX = 25.0
    elif _alter_y <= 44:
        BMI_MIN = 21.0
        BMI_MAX = 26.0
    elif _alter_y <= 54:
        BMI_MIN = 22.0
        BMI_MAX = 27.0
    elif _alter_y <= 64:
        BMI_MIN = 23.0
        BMI_MAX = 28.0
    else:
        BMI_MIN = 24.0
        BMI_MAX = 29.0

    return _bmi


def ausgabe(_bmi):
    # ----------- Ausgabe ---------------
    print(" Ihr BMI beträgt:", _bmi)
    if _bmi < BMI_MIN:
        print(" zu dünn")
    elif _bmi > BMI_MAX:
        print(" zu dick")
    else:
        print(" normal")


# ---------- main -----------------
masse_kg, groesse_m, alter_y = eingabe()  # Aufruf der Funktion
bmi = verarbeitung(masse_kg, groesse_m, alter_y)
ausgabe(bmi)

print("ENDE")


