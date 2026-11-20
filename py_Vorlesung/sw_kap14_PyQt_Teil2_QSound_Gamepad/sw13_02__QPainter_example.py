
import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class MeinFenster(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPainter Beispiel")
        self.resize(400, 300)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Füllfarbe festlegen
        painter.setBrush(QColor("red"))

        # Keine Umrandung
        painter.setPen(Qt.PenStyle.NoPen)

        # Roten Kreis zeichnen
        painter.drawEllipse(50, 100, 60, 60)

        painter.end()


# Hauptprogramm
if __name__ == "__main__":
    app = QApplication(sys.argv)

    fenster = MeinFenster()
    fenster.show()

    sys.exit(app.exec())
