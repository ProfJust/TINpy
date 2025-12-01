# qt_wuerfel_pyqt6.py  ===> VORGABE
import sys
import random
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCheckBox,
    QPushButton,
    QLabel
)
from PyQt6.QtCore import QRect


class QtWuerfel(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Qt Würfel (PyQt6)")
        self.setFixedSize(600, 400)

        # Liste für die 7 Checkboxes (Augen des Würfels)
        self.liste_checkboxes: list[QCheckBox] = []

        # Geometrie-Daten wie im C++-Code
        liste_geometry = [
            (50,  50, 100, 60),
            (50, 150, 100, 60),
            (50, 250, 100, 60),
            (250,  50, 100, 60),
            (250, 150, 100, 60),
            (250, 250, 100, 60),
        ]

        # Gemeinsames Stylesheet für runde, große Checkbox-Indikatoren
        checkbox_stylesheet = """
        QCheckBox::indicator {
            width: 50px;
            height: 50px;
            border-radius: 25px;
        }
        QCheckBox::indicator:unchecked {
            border: 1px dotted #999;
        }
        QCheckBox::indicator:checked {
            background-color: #007bff;
            border: 2px solid #005cbf;
        }
        """

        # 6 Checkboxes erzeugen
        for i, (x, y, w, h) in enumerate(liste_geometry):
            cb = QCheckBox(str(i), self)
            cb.setStyleSheet(checkbox_stylesheet)
            cb.setChecked(True)
            cb.setEnabled(True)
            cb.setGeometry(QRect(x, y, w, h))
            self.liste_checkboxes.append(cb)

        # Label für das Ergebnis
        #### HIER CODE EINFÜGEN #####

        # "Würfeln"-Button
        #### HIER CODE EINFÜGEN #####

        # In Python reicht das globale random-Modul (entspricht srand + rand)
        #### HIER CODE EINFÜGEN #####

    def wurf_btn_slot(self):
        """Slot, der beim Klick auf den 'Würfeln'-Button aufgerufen wird."""
        # Zufallszahl 1..7 (wie (rand() % 7) + 1 im C++-Code)
        result = 1  ##### HIER CODE EINFÜGEN #####
        
        # Ausgabe auf Label
        #### HIER CODE EINFÜGEN #####
       

        cb = self.liste_checkboxes
        # Erst alle Augen ausschalten (spart Schreibarbeit)
        for c in cb:
            c.setChecked(False)

        # Muster wie im C++-switch
        if result == 1:
            cb[6].setChecked(True)
        elif result == 2:
            cb[0].setChecked(True)
            cb[5].setChecked(True)
        


def main():
    app = QApplication(sys.argv)
    w = QtWuerfel()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
