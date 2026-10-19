drehzahl = [1000, 1010, 990, 1020, 1005, 1800,
            1010, 1020, 1030, 1200, 1400, 1600, 1800]

for i, wert in enumerate(drehzahl):
    differenz = 0
    if i >= 1:  # Index i-1 muss in der Liste sein
        differenz = abs(drehzahl[i] - drehzahl[i-1])

    if differenz > 200:
        print("Ausreißer!")

    print(f"Nr. {i:02d} {wert} U/min")
