
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton
)


class MeinFenster(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit Beispiel")

        # Layout erzeugen
        layout = QVBoxLayout()

        # Eingabefeld erzeugen
        self.eingabe = QLineEdit()
        self.eingabe.setPlaceholderText("Name eingeben")

        # Button erzeugen
        self.button = QPushButton("Übernehmen")
        self.button.clicked.connect(self.ausgabe)

        # Label für Ausgabe
        self.label = QLabel("Noch keine Eingabe")

        # Widgets zum Layout hinzufügen
        layout.addWidget(self.eingabe)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)
        # ausgabe() wird beim Drücken der Enter-Taste ausgeführt.
        self.eingabe.returnPressed.connect(self.ausgabe)  
        
    def ausgabe(self):
        text = self.eingabe.text()
        self.label.setText("Eingabe: " + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenster = MeinFenster()
    fenster.show()
    sys.exit(app.exec())
