# ue01_ws26_bmi.py
# Übung 01 TINpy WS26
# Last edited 15.10.26 by OJ
# Berechnet den Body Mass Index

# Eingabe
def eingabe_fkt():
    gewicht_kg = float(input("Gewicht in kg: "))
    print(" Sie haben eingegeben: ", gewicht_kg, " kg")
    laenge_m = float(input("Größe in m: "))
    print(" Sie haben eingegeben: ", laenge_m, " m")
    alter_jahre = float(input("Alter in Jahren: "))
    print(" Sie haben eingegeben: ", alter_jahre, " Jahre")
    return gewicht_kg, laenge_m, alter_jahre


# Verarbeitung
def verarbeitung_fkt(gewicht_kg,  laenge_m, alter_jahre):
    my_bmi = 0  # Ergebnis
    BMI_MAX = 25
    BMI_MIN = 18.5
    ausgabetext = "leerer String"
    my_bmi = gewicht_kg / laenge_m**2
    print(f" BMI:  {my_bmi:.1f}")

    if alter_jahre < 19:
        print("zu jung")
    if 19 <= alter_jahre <= 24:
        BMI_MAX = 24
        BMI_MIN = 19
    if 25 <= alter_jahre <= 34:
        BMI_MAX = 25
        BMI_MIN = 20
    if 35 <= alter_jahre <= 44:
        BMI_MAX = 26
        BMI_MIN = 21
    if 45 <= alter_jahre <= 54:
        BMI_MAX = 27
        BMI_MIN = 22
    if 55 <= alter_jahre <= 64:
        BMI_MAX = 28
        BMI_MIN = 23
    if alter_jahre > 64:
        BMI_MAX = 29
        BMI_MIN = 24

    if my_bmi < BMI_MIN:
        _ausgabetext = " zu dünn"
    else:
        if my_bmi >= BMI_MAX:
            _ausgabetext = " zu dick"
        else:
            _ausgabetext = " normal "
    return _ausgabetext


# --------------------------------------------
# main
g_gewicht_kg, g_laenge_m, g_alter_jahre = eingabe_fkt()
ausgabetext = verarbeitung_fkt(g_gewicht_kg, g_laenge_m, g_alter_jahre)
# ausgabetext = verarbeitung_fkt(eingabe_fkt())
# Ausgabe
print(ausgabetext)
