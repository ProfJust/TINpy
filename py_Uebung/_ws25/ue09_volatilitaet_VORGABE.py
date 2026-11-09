import math
import os

kurswerte = []


def werte_aus_datei_lesen():
    print("\n Werte aus Datei lesen")
    #### HIER CODE EINFÜGEN ####
    


def ausgabe_liste(numb_of_data):
    print("\n AusgabeListe()")
    #### HIER CODE EINFÜGEN ####


def mittelwert(numb_of_data):
    sum_m = 0.0
    #### HIER CODE EINFÜGEN ####
    


def volatilitaet(numb_of_data):
    m = mittelwert(numb_of_data)
    sum_v = 0.0
     #### HIER CODE EINFÜGEN ####


def main():
    # ab d)
    noE = werte_aus_datei_lesen()
    print(f" Ausgabe der {noE} Kurswerte")
    ausgabe_liste(noE)

    print(" Berechnung des Mittelwertes: ", end="")
    print(mittelwert(noE))

    print(" Berechnung der Volatilitaet: ", end="")
    print(volatilitaet(noE))


if __name__ == "__main__":
    # ==> In den Arbeitsordner wechseln 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    main()
