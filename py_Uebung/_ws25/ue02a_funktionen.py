# # def begruessung():
# #     print("Hello Tinpy-World!")


# # begruessung()
# # begruessung()
# # begruessung()


# def rechteck_flaeche(breite, hoehe):
#     flaeche = breite * hoehe
#     # print(flaeche)
#     return flaeche


# def celsius_to_fahrenheit(celsius):
#     fahrenheit = celsius * 1.8 + 32
#     return fahrenheit


# list_cels = list(range(0, 101, 5))  # Liste bilden
# print(list_cels)
# list_fahr = []
# for cels in list_cels:
#     fahr = celsius_to_fahrenheit(cels)
#     # print(fahr)
#     list_fahr.append(fahr)

# print(list_fahr)

def berechne_strecke(geschwindigkeit, zeit):
    strecke = geschwindigkeit * zeit  # s=v*t
    ausgabe_strecke(strecke)  # Aufruf der Funktion
    return strecke


def ausgabe_strecke(strecke):   # Definition
    print(f" Strecke {strecke:0.2f} m")


v = 0.25  # m/s
t = 12  # Sekunden
# Funktionen aufrufen
s = berechne_strecke(v, t)
