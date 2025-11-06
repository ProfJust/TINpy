import math

class Vektor:
    # Konstruktor
    def __init__(self, name="no name", a=0.0, b=0.0, c=0.0):
        self.werte = [a, b, c]
        self.name = name

    def ausgabe(self):
        print(f"--- Vektor {self.name} ---")
        for i, wert in enumerate(self.werte):
            print(f"Wert {i}: {wert}")
        # for wert in self.werte:
        #     print(f"{wert}")

    @staticmethod
    def  skalarprodukt(v1, v2):
        return sum([v1.werte[i] * v2.werte[i] for i in range(3)])
    
    # def  skalarprodukt(self, other):
    #     skalarprodukt = (self.werte[0] * other.werte[0] +
    #                      self.werte[1] * other.werte[1] +
    #                      self.werte[2] * other.werte[2]
    #                     )
    #     return skalarprodukt
    # Alternaive mit List Comprehension
    # return sum([self.werte[i] * other.werte[i] for i in range(3)])
    
    def __mul__(self, other):  
        """ Operatorzeichen '*' überladen mit __mul__ """
        # return self.skalarprodukt(other)
        return Vektor.skalarprodukt(self, other)
    
    def vektorprodukt(self, other):        
        a1, a2, a3 = self.werte
        b1, b2, b3 = other.werte
        c1 = a2 * b3 - a3 * b2
        c2 = a3 * b1 - a1 * b3
        c3 = a1 * b2 - a2 * b1
        return Vektor(name=f"{self.name}x{other.name}", a=c1, b=c2, c=c3)

    def __pow__(self, other):  # pow ist der '**' Operator
        return self.vektorprodukt(other)
    
    def vektoraddition(self, other):
        erg = Vektor()
        erg.werte[0] = self.werte[0] + other.werte[0]
        erg.werte[1] = self.werte[1] + other.werte[1]
        erg.werte[2] = self.werte[2] + other.werte[2]
        erg.name = 'Vektoraddition'
        return erg
    
    def betrag(self):
        erg = math.sqrt(self.werte[0]**2 + self.werte[1]**2 + self.werte[2]**2 )
        return erg
    
    def __add__(self, other):
        return self.vektoraddition(other)



# --- main ---
if __name__== '__main__':
    v1  = Vektor("X",3.0, 2.0 ,1.0 )  # aufruf des Konstruktors
    v1.ausgabe()
    v2  = Vektor("Y",1.0, 2.0 ,3.0 )  # aufruf des Konstruktors
    v2.ausgabe()

    #ergebnis = v1.skalarprodukt(v2)
    ergebnis = Vektor.skalarprodukt(v1, v2)
    print("Skalarprodukt: ", ergebnis)
    ergebnis2 = v1*v2
    print("Skalarprodukt mit Operator: ", ergebnis2)

    erg_vektor = v1.vektorprodukt(v2)
    erg_vektor.ausgabe()
    erg_vektor2 = v1 ** v2
    erg_vektor2.ausgabe()

    erg_vektor3 = v1 + v2
    erg_vektor3.ausgabe()

    v3  = Vektor("X",1.0, 1.0 ,0.0 ) 
    print(" Betrag: ", v3.betrag())