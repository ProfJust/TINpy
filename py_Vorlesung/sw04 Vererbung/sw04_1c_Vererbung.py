
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

# Vererbung 2   
class Fts(Roboter):  # Fahrerloses Transportsystem
    def __init__(self, name, hersteller, aufgaben):
        super().__init__(name, hersteller)
        self.aufgaben = aufgaben

    def fuehre_aufgabe_aus(self):
        return f"{self.name} führt die Aufgaben '{self.aufgaben}' aus."

#--------------------------------------------------------------------
if __name__ == '__main__':
    robo = Roboter('youBot', 'Kuka')
    print(robo.starte())
    print(robo.stoppe())

    roboArm = Roboterarm('IRB 1200-5', 'ABB', 5)
    print(roboArm.hebe_last())

    fts = Fts('T300', 'Pudu',['Transport','Navigation'])
    print(fts.fuehre_aufgabe_aus())


