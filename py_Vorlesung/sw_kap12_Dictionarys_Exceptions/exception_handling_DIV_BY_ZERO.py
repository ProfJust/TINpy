eingabe = 0
inputOK = False

while not inputOK:
    try:
        eingabe = input("Geben Sie eine Zahl ein! ")
        zahl = eval(eingabe) # built in function eval(): str => int
        ergebnis = 1/zahl
        inputOK = True

    except NameError:
        print(" Eingabe war keine gültige Zahl")
        break  # ENde der While Schleife

    except ZeroDivisionError:
        print( "Error:  Division durch Null! ")
        break

    print(f" l/ %d  = %f " % (zahl, ergebnis)) # Ausgabe im C-Style

# print(" Ende des Programms erreicht")
