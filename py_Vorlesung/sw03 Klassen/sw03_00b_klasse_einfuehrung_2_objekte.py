from time import sleep
dt = 0.5  # sec


class Roboter:  # Definiert die Klasse

    def fahren(self, v):   # Methode mit einem Parameter
        self.geschwindigkeit = v
        print(f"Roboter fährt mit {v} m/s")

    def stoppen(self):
        self.geschwindigkeit = 0
        print("Roboter steht")

    def abstand_ermitteln(self):
        # Attribute der Klasse => self voranstellen
        self.abstand -= self.geschwindigkeit * dt
        return self.abstand


# --------------------------------------------------------------------
if __name__ == '__main__':
    # Ein Objekt erzeugen
    roboter1 = Roboter()   # Instanzierung
    roboter1.abstand = 20  # Attribut initialisieren
    roboter1.fahren(0.5)   # Methode mit Parameter aufrufen

    roboter2 = Roboter()   # Instanzierung
    roboter2.abstand = 100  # Attribut initialisieren
    roboter2.fahren(1.5)   # Methode mit Parameter aufrufen
    

    while True:
        abstand = roboter1.abstand_ermitteln()
        print(f" Abstand: {abstand}")
        # Ruft eine Methode der Klasse auf
        if abstand > 10:
            roboter1.fahren(3.1)
        else:
            roboter1.stoppen()
            break  # Ende der Schleife

        abstand = roboter2.abstand_ermitteln()
        print(f" Abstand: {abstand}")
        # Ruft eine Methode der Klasse auf
        if abstand > 10:
            roboter2.fahren(5.1)
        else:
            roboter2.stoppen()
        
        sleep(dt)    # dt  warten
    print("Programm beendet")

# def __init__(self):   # Initialisierung
    #     self.abstand = 20