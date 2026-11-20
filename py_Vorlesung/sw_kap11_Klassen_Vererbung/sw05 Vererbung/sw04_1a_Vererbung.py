
# Elternklasse 
class Roboter:
    def __init__(self, name, hersteller):
        self.name = name
        self.hersteller = hersteller

    def starte(self):
        return f"{self.name} wird gestartet..."

    def stoppe(self):
        return f"{self.name} wird gestoppt."
    
#--------------------------------------------------------------------
if __name__ == '__main__':
    robo = Roboter('youBot', 'Kuka')
    print(robo.starte())
    print(robo.stoppe())


