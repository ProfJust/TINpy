
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QPushButton
)


class MeinFenster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Beispiel")
        self.resize(350, 250)

        # Grid-Layout erzeugen
        layout = QGridLayout()

        # 3 Zeilen und 3 Spalten
        for zeile in range(3):
            for spalte in range(3):
                nr = zeile * 3 + spalte + 1
                button = QPushButton(f"{nr}")
                # Button im Raster platzieren
                layout.addWidget(button, zeile, spalte)
                # Klick-Signal verbinden
                button.clicked.connect(
                    lambda checked=False, n=nr: self.geklickt(n)
                )
        self.setLayout(layout)

    def geklickt(self, nummer):
        print(f"Button {nummer} wurde geklickt")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    fenster = MeinFenster()
    fenster.show()

    sys.exit(app.exec())
