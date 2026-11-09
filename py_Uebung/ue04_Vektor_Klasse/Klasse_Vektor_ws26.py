# TEst für Vektorprodukt in Aufgabenstellung
# Indizes auf 0,1,2 ändern in der Rechenvorschrift
# GitHub Lösung entfernern

class Vektor:
    def __init__(self, name="no name", a=0.0, b=0.0, c=0.0):
        self.werte = [a, b, c]
        self.name = name

    def ausgabe(self):
        print(f"--- Vektor {self.name} ---")
        for i, wert in enumerate(self.werte):
            print(f"Wert {i}: {wert}")

    def skalarprodukt(self, other):
        # Zeilenumbruch mit Backslash "\"
        ergebnis = self.werte[0] * other.werte[0] +\
                   self.werte[1] * other.werte[1] +\
                   self.werte[2] * other.werte[2]
        return ergebnis
    #  return sum(a * b for a, b in zip(self.werte, other.werte))  Listenabstraktion zip() sum()

    def __mul__(self, other):
        return self.skalarprodukt(other)

    def kreuzprodukt(self, other):
        # Zeilenumbruch mit () Klammern
        erg_vektor = ([self.werte[1] * other.werte[2] 
                      - self.werte[2] * other.werte[1],
                      self.werte[2] * other.werte[0] 
                      - self.werte[0] * other.werte[2],
                      self.werte[0] * other.werte[1] 
                      - self.werte[1] * other.werte[0]]
                      )
        return erg_vektor
    
    def __mod__(self, other):
        return self.kreuzprodukt(other)


# --- Testprogramm der Klasse
if __name__ == "__main__":
    a = Vektor("A", 1, 2, 3)
    a.ausgabe()
    b = Vektor("B", 2, 3, 4)
    b.ausgabe()

    print("Skalarprodukt", a.skalarprodukt(b))
    print("Skalarprodukt mit Operator * ", a * b)
    print(a.name, " * ", b.name, " = ", a.skalarprodukt(b))

    print("Kreuzprodukt", a.kreuzprodukt(b))
    print("Kreuzprodukt mit Operator * ", a % b)
    print(a.name, " x ", b.name, " = ", a.kreuzprodukt(b))
    
