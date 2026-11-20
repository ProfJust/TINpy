
class Roboter:  # Elternklasse
    def __init__(self, name):
        self.name = name

    def fahren(self):
        print(f"{self.name} fährt.")

    def stoppen(self):
        print(f"{self.name} stoppt.")


# MobilerRoboter erbt von Roboter
class MobilerRoboter(Roboter):  # Kindklasse(Elternklasse)

    def position_anzeigen(self):
        print(f"{self.name}: Position anzeigen")

    def stoppen(self):
        print(f"{self.name} Mobiler Roboter stoppt.")


# Objekt der abgeleiteten Klasse erzeugen
robot1 = MobilerRoboter("TurtleBot3")

robot1.fahren()   # Methode der Elternklasse
robot1.stoppen()  # Methode der Elternklasse oder Kindklasse?
robot1.position_anzeigen()  # Methode der Kindklasse
