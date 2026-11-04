
def klassifizieren(abstand):
    if abstand < 20:
        return "STOPP"
    elif abstand < 50:
        return "WARNUNG"
    else:
        return "FREI"


# --------------------------------------------------------------------
if __name__ == '__main__':
    abstand = 35
    klasse = klassifizieren(abstand)

    print("Klasse:", klasse)   # Ausgabe => Klasse: WARNUNG
