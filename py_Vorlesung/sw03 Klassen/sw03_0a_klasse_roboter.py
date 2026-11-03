
class Roboter:  # Definiert die Klasse
    anzahl = 0   # Klassenvariable
    # Initialisierungsmethode, wird beim Erzeugen eines Objekts aufgerufen
    def __init__(self, name):
        # Nicht so anzahl += 1
        # Greifen Sie über den Klassennamen auf die Klassenvariable zu
        Roboter.anzahl += 1
        self.name = name        # self => Referenz auf das aktuelle Objekt
        self.geschwindigkeit = 0  # Attribut des Objekts

    def fahren(self, v):   # Methode mit einem Parameter
        self.geschwindigkeit = v
        print(f"{self.name} fährt mit {v} m/s")

    def stoppen(self):
        self.geschwindigkeit = 0
        print(f"{self.name} steht")


# Zwei Objekte erzeugen
roboter1 = Roboter("TurtleBot3")
print(Roboter.anzahl)
roboter2 = Roboter("Alvik")
print(Roboter.anzahl)

# Ruft eine Methode auf
roboter1.fahren(0.2)
roboter2.fahren(0.1)
roboter1.stoppen()
