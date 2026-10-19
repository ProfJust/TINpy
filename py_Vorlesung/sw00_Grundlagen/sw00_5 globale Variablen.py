# ------------------------------------------------
# --- global_and_local_Var.py ----
# Version vom 18.09.2026 by OJ
# -------------------------------------------------
# WHS - Campus Bocholt - TINpy
# globale Variablen - Demo
# -------------------------------------------------

# globale Variable
summe = 0


def summiere(upto):
    for i in range(1, upto+1, 1):
        global summe  # Zugriff auf globale Variable
        summe += 1    # gewünschter Zugriff auf globale Variable


if __name__ == "__main__":  # Das Hauptprogramm
    summiere(10)
    print(summe)
