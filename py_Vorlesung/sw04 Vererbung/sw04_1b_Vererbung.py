
# Elternklasse 
class Roboter:
    def __init__(self, name, hersteller):
        self.name = name
        self.hersteller = hersteller

    def starte(self):
        return f"{self.name} wird gestartet..."

    def stoppe(self):
        return f"{self.name} wird gestoppt."
    
# Vererbung 1
class Roboterarm(Roboter):  # <=== Elternteil in ()
    def __init__(self, name, hersteller, tragkraft): # in kg
        super().__init__(name, hersteller)  # <=== Aufruf Konstruktor Elternklasse
        self.tragkraft = tragkraft

    def hebe_last(self):
        return f"{self.name} hebt eine Last von {self.tragkraft} kg."

#--------------------------------------------------------------------
if __name__ == '__main__':
    robo = Roboter('youBot', 'Kuka')
    print(robo.starte())
    print(robo.stoppe())

    roboArm = Roboterarm('Ur3e', 'Universal Robot', 3)
    print(roboArm.hebe_last())

