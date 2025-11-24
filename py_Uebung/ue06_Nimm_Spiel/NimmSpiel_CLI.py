import random
import time
from enum import Enum

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Globale Variablen
w_hoelzer = 0  # Die aktuelle Anzahl der Hölzer
w_zug = 0      # Der aktuelle Zug des Spielers
w_computer_zug = 0  # Der aktuelle Zug des Rechners

class EreignisTyp(Enum):
    AKTIV = 1
    GEWONNEN = 2
    VERLOREN = 3

spiel_zustand = EreignisTyp.AKTIV  # Instanz von EreignisTyp

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def hole_zufallszahl(w_von: int, w_bis: int) -> int:
    return random.randint(w_von, w_bis)

def gebe_anz_hoelzer_aus(w_anzahl: int) -> None:
    if w_anzahl > 1:
        print(f"{w_anzahl} Hölzer sind im Spiel")
    else:
        print(f"{w_anzahl} Holz ist im Spiel")

def eingabe_zug(h: int) -> int:
    while True:
        try:
            w_eingabe = int(input("\nIhr Zug bitte: "))
            if w_eingabe < 1 or w_eingabe > 3:
                print("\nEingabefehler, nur 1, 2 oder 3 ist möglich!!")
            elif w_eingabe > h:
                print(f"\nNur noch {h} Hölzer vorhanden!")
            else:
                return w_eingabe
        except ValueError:
            print("\nBitte eine Zahl eingeben!")

def pruef_ob_gewonnen(h: int) -> EreignisTyp:
    if h == 1:
        print("\n\nSpiel gewonnen!!!\n")
        return EreignisTyp.GEWONNEN
    if h == 0:
        print("\n\nSpiel verloren!!!\n")
        return EreignisTyp.VERLOREN
    return EreignisTyp.AKTIV

def hole_computer_zug(h: int) -> int:
    # Strategie
    match h:    #  Python 3.10+ unterstützt match/case für Switch-ähnliche Logik.
        case 1:
            return 1
        case 2:
            return 1
        case 3:
            return 2
        case 4:
            return 3
        case 6:
            return 1
        case 7:
            return 2
        case 8:
            return 3
        case _:
            return hole_zufallszahl(1, 3)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():
    global w_hoelzer, w_zug, w_computer_zug, spiel_zustand
    # Initialisierung des Zufallsgenerators mit Systemstartzeit
    random.seed(int(time.time()))
    w_hoelzer = hole_zufallszahl(16, 25)  # Ermittlung einer Zufallszahl von 16..25
    gebe_anz_hoelzer_aus(w_hoelzer)

    # Die Hauptschleife
    while spiel_zustand == EreignisTyp.AKTIV:
        w_zug = eingabe_zug(w_hoelzer)  # Zug vom Benutzer holen
        w_hoelzer -= w_zug
        gebe_anz_hoelzer_aus(w_hoelzer)
        spiel_zustand = pruef_ob_gewonnen(w_hoelzer)
        if spiel_zustand == EreignisTyp.AKTIV:
            w_computer_zug = hole_computer_zug(w_hoelzer)
            w_hoelzer -= w_computer_zug
            print(f"\nDer Computer hat {w_computer_zug} Hölzer genommen\n")
            gebe_anz_hoelzer_aus(w_hoelzer)

if __name__ == "__main__":
    main()
