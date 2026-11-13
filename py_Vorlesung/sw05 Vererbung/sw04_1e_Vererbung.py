class Roboter:
    def __init__(self, name, hersteller, **kwargs):
        self.name = name
        self.hersteller = hersteller

    def starte(self):
        return f"{self.name} wird gestartet..."

    def stoppe(self):
        return f"{self.name} wird gestoppt."

class Roboterarm(Roboter):
    def __init__(self, name, hersteller, tragkraft=None, **kwargs):
        super().__init__(name, hersteller, **kwargs)
        self.tragkraft = tragkraft

    def hebe_last(self):
        return f"{self.name} hebt eine Last von {self.tragkraft} kg."

class CobotArm(Roboterarm):
    def __init__(self, name, hersteller, tragkraft=None, **kwargs):
        super().__init__(name, hersteller, tragkraft=tragkraft, **kwargs)

    def Kollision_erkannt(self) -> str:
        return "Kollision Armbewegung erkannt"

class Fts(Roboter):
    def __init__(self, name, hersteller, aufgaben=None, **kwargs):
        super().__init__(name, hersteller, **kwargs)
        self.aufgaben = aufgaben

    def fuehre_aufgabe_aus(self):
        return f"{self.name} führt die Aufgaben '{self.aufgaben}' aus."

class HybridRobo(CobotArm, Fts):
    def __init__(self, name, hersteller, tragkraft, aufgaben):
        super().__init__(name, hersteller, tragkraft=tragkraft, aufgaben=aufgaben)
    
    # Überschreibt die gleichnamige Funktion der Elternklasse
    def Kollision_erkannt(self) -> str:
        return "Kollision bei der Navigation erkannt"

if __name__ == '__main__':
    hybrid_robo = HybridRobo('HybridBot', 'Kuka', 3, 'Transportieren')
    print(hybrid_robo.starte())
    print(hybrid_robo.Kollision_erkannt())
    print(hybrid_robo.fuehre_aufgabe_aus())
