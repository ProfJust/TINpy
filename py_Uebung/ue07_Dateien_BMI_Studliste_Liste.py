""" TINpy UE07
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
        # print(dateipfad)
        if not dateipfad.exists():
            raise FileNotFoundError(f"Die Datei '{dateipfad}' wurde nicht gefunden!")

        print("Werte aus Datei werden gelesen")
        with dateipfad.open("r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                weight, size = line.strip().split() # Text-Zeile am Leerzeichen aufteilen
                self.data.append( [weight, size] ) # Wertepaar dem Schlüssel [i] zuweisen 
                print(f"{i}  {self.data[i][0]} {self.data[i][1]}")  # Debug Ausgabe     

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
        for [weight, size] in self.data:  # Werte als Zeichenkette
            if index == 0:
                self.data[0] = self.data[0] + ['BMI'] # Ergänze Titelzeile      
            if index >0:  # Titelzeile ignoriere: "Gewicht" ist keine Zahl
                bmi = eval(weight) / eval(size)**2
                print(f"BMI: {bmi}")
                self.data[index] = self.data[index] + [bmi,]
            index +=1
        print("\n Das erweiterte Dictionary")
        print(self.data)

    def showBMI(self):
        print("\n SHOW BMI")
        index = 0
        for [weight, size, bmi] in self.data:  # Schlüssel und die (Liste der Werte)
            if index == 0:
                print(f"{index} ,  {weight} ,  {size} , {bmi}")
            else:
                print(f"{index} Gewicht/kg {weight}, Größe/m {size} , BMI {bmi}")
            index += 1

        print(f"Anzahl der gelesenen Datensätze: {index-1}")
        return index
   
    def writeFile(self, dateiname):
        # Ordner, in dem dieses Skript liegt
        script_dir = Path(__file__).resolve().parent
        # Dateipfad zusammenfügen 
        dateipfad = script_dir / dateiname
       
        with dateipfad.open("w", encoding="utf-8") as f:
            for values in self.data:
                f.write(f"{values}\n")

    # Variante 1
    # def calcAVG(self):
    #     summe=0
    #     anz = 0
    #     for [weight, size, bmi] in self.data:
    #         if anz > 0: 
    #             summe += float(bmi) # statt eval
    #         anz +=1
    #     ergebnis = summe / (anz-1)
    #     return ergebnis

    # Variante 2
    def calcAVG(self):
        summe=0
        index = 0
        for [weight, size, bmi] in self.data:
            # Werte (values) können z.B. ['Gewicht','Größe','BMI'] (Header) oder [weight, size, bmi] sein
            try:
                bmi = float(bmi)
                summe += bmi
            except (ValueError, TypeError):
                    # Nicht-numerischer Eintrag (z.B. Header) überspringen
                    pass
            index += 1

        ergebnis = summe / (index-1)
        return ergebnis


#--------------------------------------------------------------------
if __name__ == '__main__':
    list = StudiListe()
    # ErrorTest mit  test list.readFile("Studenten_Gewicht_Groesse2.txt")
    list.readFile("Studenten_Gewicht_Groesse.txt")
    #list.show()
    list.calcBMI()
    list.showBMI()
    list.writeFile("Studenten_Gewicht_Groesse_BMI.txt")
    print("Durchschnittlicher BMI :", list.calcAVG())


