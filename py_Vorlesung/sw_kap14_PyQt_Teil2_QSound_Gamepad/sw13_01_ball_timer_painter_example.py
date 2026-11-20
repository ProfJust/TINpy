
import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QPainter, QColor, QBrush


class MeinFenster(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QPainter mit QTimer")
        self.resize(600, 400)

        # Position und Bewegung des Kreises
        self.x = 50
        self.y = 200
        self.radius = 25
        self.vx = 5

        # Timer erzeugen
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.bewegen)
        self.timer.start(20)  # 20 ms / 50Hz

    def bewegen(self):
        # Neue Position berechnen
        self.x += self.vx

        # Am Fensterrand Richtung umkehren
        if self.x + self.radius >= self.width():
            self.vx = -abs(self.vx)

        if self.x - self.radius <= 0:
            self.vx = abs(self.vx)

        # Neuzeichnen anfordern
        self.update()

    def paintEvent(self, event):
        # QPainter zum Zeichnen verwenden
        painter = QPainter(self)

        # Hintergrund weiß
        painter.fillRect(self.rect(), QColor("white"))

        # Roten Kreis zeichnen
        painter.setBrush(QBrush(QColor("red")))
        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(
            int(self.x - self.radius),
            int(self.y - self.radius),
            2 * self.radius,
            2 * self.radius
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    fenster = MeinFenster()
    fenster.show()

    sys.exit(app.exec())
