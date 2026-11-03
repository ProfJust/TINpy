
# Datei: roboter.py

class Roboter:

    anzahl = 0  # Klassenvariable

    def __init__(self, name):
        Roboter.anzahl += 1
        self.name = name
        self.geschwindigkeit = 0

    def fahren(self, v):
        self.geschwindigkeit = v
        print(f"{self.name} fährt mit {v} m/s")

    def stoppen(self):
        self.geschwindigkeit = 0
        print(f"{self.name} steht")

    def __str__(self):
        return f"Roboter: {self.name}"
