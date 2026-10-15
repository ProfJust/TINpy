# ue01_ws26_bmi.py
# Übung 01 TINpy WS26
# Last edited 15.10.26 by OJ

# Berechnet den Body Mass Index

# Initialisierung
my_bmi = 0  # Ergebnis
BMI_MAX = 25
BMI_MIN = 18.5 
ausgabetext = "leerer String"

# Eingabe
gewicht_kg = 95.5  # float(input("Gewicht in kg: "))
print(" Sie haben eingegeben: ", gewicht_kg, " kg")

laenge_m = 1.95  # float(input("Größe in m: "))
print(" Sie haben eingegeben: ", laenge_m, " m")

# Verarbeitung
my_bmi = gewicht_kg / laenge_m**2
print(f" BMI:  {my_bmi:.1f}")

if my_bmi < BMI_MIN:
    ausgabetext = " zu dünn"
else:
    if my_bmi >= BMI_MAX:
        ausgabetext = " zu dick"
    else:
        ausgabetext = " normal "

# Ausgabe
print(ausgabetext)
