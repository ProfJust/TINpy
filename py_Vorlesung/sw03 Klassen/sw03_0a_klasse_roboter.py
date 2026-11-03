
class Roboter:  # Definiert die Klasse

    # Initialisierungsmethode, wird beim Erzeugen eines Objekts aufgerufen
    def __init__(self, name):
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
roboter2 = Roboter("Alvik")

# Ruft eine Methode auf
roboter1.fahren(0.2)
roboter2.fahren(0.1)

roboter1.stoppen()
