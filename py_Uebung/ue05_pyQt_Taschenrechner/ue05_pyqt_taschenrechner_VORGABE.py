
import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QMessageBox,
    QVBoxLayout, QHBoxLayout
)


class Taschenrechner(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 - Taschenrechner")
        self.resize(350, 250)

        # Hauptlayout
        layout = QVBoxLayout()

        # Eingabefelder
        self.zahl1 = QLineEdit()
        self.zahl1.setPlaceholderText("Zahl 1 eingeben")

        layout.addWidget(QLabel("Zahl 1:"))
        layout.addWidget(self.zahl1)

        # Buttons für die Grundrechenarten
        button_layout = QHBoxLayout()

        ### HIER CODE EINFÜGEN ####

        self.btn_plus = QPushButton("+")
        button_layout.addWidget(self.btn_plus)
        
        layout.addLayout(button_layout)

        # Ergebnisanzeige
        self.ergebnis = QLabel("Ergebnis: --")
        layout.addWidget(self.ergebnis)

        # Signale mit Methoden verbinden
        self.btn_plus.clicked.connect(
            lambda: self.berechnen("+")
        )       

        self.setLayout(layout)

    # ---------------------------------------
    # Berechnung
    # ---------------------------------------
    def berechnen(self, operator):

        try:
            a = float(self.zahl1.text())

            ### HIER CODE EINFÜGEN ####

        except ValueError:
            QMessageBox.warning(
                self,
                "Eingabefehler",
                "Bitte gültige Zahlen eingeben!"
            )
            return

        if operator == "+":
            ergebnis = a + a


        ### HIER CODE EINFÜGEN ####

        self.ergebnis.setText(
            f"Ergebnis: {ergebnis:.2f}"
        )

    # ---------------------------------------
    # Eingaben zurücksetzen
    # ---------------------------------------
    def reset(self):
        pass
        ### HIER CODE EINFÜGEN ####
        # self.zahl1.clear()
        

# -------------------------------------------
# Hauptprogramm
# -------------------------------------------
if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Helles Design
    # app.setStyle("Fusion")
    # app.setStyleSheet("""
    #     QWidget {
    #         background-color: white;
    #         color: black;
    #     }
    #     QLineEdit {
    #         background-color: white;
    #         border: 1px solid gray;
    #         padding: 5px;
    #     }
    #     QPushButton {
    #         background-color: #eeeeee;
    #         border: 1px solid #aaaaaa;
    #         padding: 6px;
    #     }
    #     QPushButton:hover {
    #         background-color: #dddddd;
    #     }
    # """)

    fenster = Taschenrechner()
    fenster.show()

    sys.exit(app.exec())
