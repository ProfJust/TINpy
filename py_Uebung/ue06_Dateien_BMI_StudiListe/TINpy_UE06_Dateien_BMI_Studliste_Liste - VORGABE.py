""" TINpy UE06
liest und schreibt Datensätze aus/in eine Textdatei  in eine Liste """

from pathlib import Path

class StudiListe():
    """ Klasse für eine Liste """
    def __init__(self):  # Konstruktor
        self.data = []  # Eine Liste als Datenspeicher

    def readFile(self, dateiname):
        # Ordner, in dem dieses Skript liegt
        script_dir = Path(__file__).resolve().parent
        # Dateipfad zusammenfügen 
        dateipfad = script_dir / dateiname
        if not dateipfad.exists():
            raise FileNotFoundError(f"Die Datei '{dateipfad}' wurde nicht gefunden!")
                
        print("Werte aus Datei werden gelesen")
        with dateipfad.open("r", encoding="utf-8") as f:
            pass # **** #
        
    def show(self):
        print("\n SHOW ")
        index = 0
        for [weight, size] in self.data:  # Schlüssel und die (Liste der Werte)
            print(f"{index} Gewicht/kg {weight}, Größe/m {size} ")
            index += 1

        print(f"Anzahl der gelesenen Datensätze: {index}")
        return index
            
    def calcBMI(self):
        print("\n CALC BMI")
        index = 0
       # **** #
        print("\n Das erweiterte Dictionary")
        print(self.data)

    def showBMI(self):
        print("\n SHOW BMI")
        index = 0
        # **** #
        print(f"Anzahl der gelesenen Datensätze: {index}")
        return index
    
    def writeFile(self, dateiname):
        # **** #
        pass


#--------------------------------------------------------------------
if __name__ == '__main__':
    list = StudiListe()
    # ErrorTest mit  test list.readFile("Studenten_Gewicht_Groesse2.txt")
    list.readFile("Studenten_Gewicht_Groesse.txt")
    list.show()
    list.calcBMI()
    list.showBMI()
    list.writeFile("Studenten_Gewicht_Groesse_BMI.txt")


