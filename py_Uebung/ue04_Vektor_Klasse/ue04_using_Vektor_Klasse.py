from vektor import Vektor

def main():
    x = Vektor("X", 1.0, 2.0, 3.0)
    y = Vektor("Y", 4.0, 2.0, 3.0)
    erg = Vektor("erg", 0.0, 0.0, 0.0)

    x.ausgabe()
    y.ausgabe()
    
    print("Skalarprodukt:", Vektor.skalarprodukt(x, y))

    print("Skalarprodukt mit Operator:", x * y)
   
    erg = Vektor.vektorprodukt(x, y)
    print("Vektorprodukt erg = x x y:")
    erg.ausgabe()

    erg = x % y 
    print("Vektorprodukt erg = x % y ")
    erg.ausgabe()

    erg = x + y
    print("VektorAddition erg = x + y:")
    erg.ausgabe()

    print(f"Norm von {erg.gib_name()}: {erg.norm()}")


if __name__ == "__main__":
    main()
