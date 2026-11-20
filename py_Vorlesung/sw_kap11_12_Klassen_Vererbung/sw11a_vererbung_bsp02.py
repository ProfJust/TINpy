
class Roboter:  # Elternklasse
    def __init__(self, name, hersteller):
        self.name = name
        self.hersteller = hersteller

    def starte(self):
        return f"{self.name} wird gestartet..."

    def stoppe(self):
        return f"{self.name} wird angehalten..."


class Roboterarm(Roboter):  # Elternteil in ()
    def __init__(self, name, hersteller, tragkraft):
        super().__init__(name, hersteller)
        self.tragkraft = tragkraft

    def hebe_last(self):
        return f"{self.name} hebt eine Last von {self.tragkraft} kg"


class FTS(Roboter):  # Fahrerloses Transportsystem
    def __init__(self, name, hersteller, aufgabe):
        super().__init__(name, hersteller) 
        self.aufgabe = aufgabe

    def fuehre_aufgabe_aus(self):
        return f"{self.name} führt die Aufgabe '{self.aufgabe}' aus."


if __name__ == '__main__':
    robo = Roboter('youbot', 'Kuka')
    print(robo.starte())
    print(robo.stoppe())

    roboArm = Roboterarm('UR3e', 'Universal Robot', 3)
    print(roboArm.hebe_last())

    fts = FTS('T300', 'Pudu',  'Navigation')
    print (fts.fuehre_aufgabe_aus())
