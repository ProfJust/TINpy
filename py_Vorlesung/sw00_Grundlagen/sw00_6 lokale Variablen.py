# ------------------------------------------------
# Version vom 19.09.2026 by OJ
# -------------------------------------------------
# WHS - Campus Bocholt - TINpy
# lokale Variablen - Demo
# -------------------------------------------------

# globale Variable
summe = 2


def summiere(upto):
    local_summe = 0
    for i in range(1, upto+1, 1):
        local_summe+= i   
    return local_summe
               

if __name__ == "__main__":  # Das Hauptprogramm 
    summiere(3)
    print(summe)  # globale Variable wird nicht verändert

    summe = summiere(3)  # Funktionsergebnis wird in globale Variable kopiert
    print(summe)

