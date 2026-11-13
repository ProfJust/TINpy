#-------------------------------------------------------------------
# Dieser Code erstellt mit PyQt6 ein einfaches GUI-Fenster mit einem Button, 
# der beim Anklicken eine Meldung in der Konsole ausgibt.
# OJ 29.09.2025
#-------------------------------------------------------------------

# sys wird verwendet, um Programm-Argumente zu verarbeiten und das Programm später zu beenden
import sys

# Die Bibliothek PyQt6 wird genutzt, insbesondere die Widget-Elemente wie QMainWindow und QPushButton. 
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Ermöglicht das Festlegen der Fenstergröße als QSize-Objekt.
from PyQt6.QtCore import QSize   


class MainWindow(QMainWindow): # Leitet eine benutzerdefinierte Fensterklasse MainWindow von QMainWindow ab.
    def __init__(self):
        super().__init__()
        # Die zentrale Komponente ist ein Fenster, das von QMainWindow erbt. 
        # Im Konstruktor (__init__) wird das Fenster auf mindestens 300x200 Pixel gesetzt und mit einem Titel versehen.

        self.setMinimumSize(QSize(300, 200))    
        self.setWindowTitle(" TINpy - Erster Button  ")

        # erzeugt einen Button mit der Beschriftung „Klick mich“, der zum Hauptfenster (self) gehört.
        pybutton = QPushButton('Klick mich', self)

        # verknüpft das „clicked“-Signal des Buttons mit dem Slot clickSlot.
        # Wird der Button geklickt, wird clickMethod ausgeführt.
        pybutton.clicked.connect(self.clickSlot)
        
        # Der Button wird auf die Größe 100x32 Pixel gesetzt 
        pybutton.resize(100,32)
        # ..und bei x=50, y=50 im Fenster positioniert.
        pybutton.move(50, 50)        

    def clickSlot(self):
        # Die Methode clickSlot(self) wird durch das Klick-Ereignis des Buttons ausgelöst 
        print('Clicked Pyqt button.') # gibt den Text „Clicked Pyqt button.“ auf der Konsole aus.

if __name__ == "__main__":
    app = QApplication(sys.argv)  # eine Anwendung wird erzeugt
    mainWin = MainWindow()  # Ein Objekt von MainWindow wird erzeugt 
    mainWin.show()          # ..und mit mainWin.show() sichtbar gemacht.
    sys.exit( app.exec() )  # startet die Event-Schleife von Qt und sorgt für sicheres Beenden der Anwendung.
