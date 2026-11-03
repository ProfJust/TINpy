
class Roboter:

    def __init__(self, name):
        self.name = name
        self.geschwindigkeit = 0

    def fahren(self, v):
        self.geschwindigkeit = v
        print(f"{self.name} fährt mit {v} m/s")

    def stoppen(self):
        self.geschwindigkeit = 0
        print(f"{self.name} steht")


# Zwei Objekte erzeugen
roboter1 = Roboter("TurtleBot3")
roboter2 = Roboter("Alvik")

roboter1.fahren(0.2)
roboter2.fahren(0.1)

roboter1.stoppen()
