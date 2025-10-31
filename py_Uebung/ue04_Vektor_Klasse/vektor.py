class Vektor:
    def __init__(self, name="no name", a=0.0, b=0.0, c=0.0):
        self.werte = [a, b, c]
        self.name = name

    def ausgabe(self):
        print(f"--- Vektor {self.name} ---")
        for i, wert in enumerate(self.werte):
            print(f"Wert {i}: {wert}")

    def gib_name(self):
        return self.name

    @staticmethod
    def skalarprodukt(v1, v2):
        return sum([v1.werte[i] * v2.werte[i] for i in range(3)])

    def __mul__(self, other):  
        """ Operatorzeichen '*' überladen mit __mul__ """
        if isinstance(other, Vektor): # prüft, ob das Objekt other eine Instanz der Klasse Vektor ist
            # Skalarprodukt zweier Vektoren
            return self.skalarprodukt(self, other)
        else:
            raise NotImplementedError("Multiplikation nur mit Vektor möglich") # Fehlerbehandlung

    @staticmethod
    def vektorprodukt(v1, v2):
        a1, a2, a3 = v1.werte
        b1, b2, b3 = v2.werte
        c1 = a2 * b3 - a3 * b2
        c2 = a3 * b1 - a1 * b3
        c3 = a1 * b2 - a2 * b1
        return Vektor(name=f"{v1.name}x{v2.name}", a=c1, b=c2, c=c3)

    def __mod__(self, other):
        return Vektor.vektorprodukt(self, other)

    def vektoraddition(v1, v2):
        a1, a2, a3 = v1.werte
        b1, b2, b3 = v2.werte
        c1 = a1 + b1
        c2 = a2 + b2
        c3 = a3 + b3
        return Vektor(name=f"{v1.name}+{v2.name}", a=c1, b=c2, c=c3)

    def __add__(self, other):
        return Vektor.vektoraddition(self, other)

    def norm(self):
        return math.sqrt(sum([x ** 2 for x in self.werte]))
