def addieren(a, b):  # erste Funktion
    return a + b


def main():  # Funktionsname main() ist frei wählbar, aber üblich
    x = 3
    y = 5
    ergebnis = addieren(x, y)
    print(ergebnis)


if __name__ == "__main__":  # Das Hauptprogramm
    # wird nur ausgeführt, wenn die Datei direkt aufgerufen wird
    main()
   

