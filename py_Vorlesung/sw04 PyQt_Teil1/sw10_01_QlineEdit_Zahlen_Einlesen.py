
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton
)

from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import QDoubleSpinBox



class MeinFenster(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit Beispiel")

        # Layout erzeugen
        layout = QVBoxLayout()

        # Eingabefeld erzeugen
        self.eingabe = QLineEdit()
        self.eingabe.setPlaceholderText("Zahl eingeben")
        # Zahlen zwischen 0.0 und 1.0 erlauben
        validator = QDoubleValidator(0.0, 1.0, 2)
        self.eingabe.setValidator(validator)

        self.eingabe2 = QDoubleSpinBox()
        self.eingabe2.setRange(0.0, 1.0)
        self.eingabe2.setDecimals(2)
        self.eingabe2.setSingleStep(0.05)
        self.eingabe2.setSuffix(" m/s")

        # Button erzeugen
        self.button = QPushButton("Übernehmen")
        self.button.clicked.connect(self.ausgabe)

        # Label für Ausgabe
        self.label = QLabel("Noch keine Eingabe")

        # Widgets zum Layout hinzufügen
        layout.addWidget(self.eingabe)
        layout.addWidget(self.eingabe2)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)
        # ausgabe() wird beim Drücken der Enter-Taste ausgeführt.
        self.eingabe.returnPressed.connect(self.ausgabe)  
        
    def ausgabe(self):
        #     v = float(self.eingabe.text())
        v = self.eingabe2.value()
        self.label.setText(f"Geschwindigkeit: {v:.2f} m/s ")

    # def ausgabe(self):
        # if self.eingabe.hasAcceptableInput():
        #     v = float(self.eingabe.text())
        #     self.label.setText( f"Geschwindigkeit: {v:.2f} m/s"  )
        # else:
        #     self.label.setText("Ungültige Eingabe! Erlaubt: 0.0 bis 1.0"  )
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenster = MeinFenster()
    fenster.show()
    sys.exit(app.exec())
