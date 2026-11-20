
import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QTimer


class BallFenster(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ball-Teleoperation")
        self.setFixedSize(1200, 900)

        # Ballposition zu Beginn
        self.x = 300.0
        self.y = 1000.0
        self.radius = 20

        # Geschwindigkeit (Pixel/Sekunde)
        self.vx = 0.0
        self.vy = 0.0

        # Dictionary für die Tastatursteuerung
        self.steuerung = {
            Qt.Key.Key_W: (0, -5),
            Qt.Key.Key_A: (-5, 0),
            Qt.Key.Key_S: (0, 5),
            Qt.Key.Key_D: (5, 0),
            Qt.Key.Key_Space: (0, 0)
        }

        # Tastaturfokus erlauben
        self.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus
        )

        # Timer: 20 ms
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.bewegen)
        self.timer.start(20)

    # ----------------------------------
    # Tastatur auswerten
    # ----------------------------------
    def keyPressEvent(self, event):
        taste = event.key()
        # Geschwindigkeit aus Dictionary lesen
        if taste in self.steuerung:
            a, b = self.steuerung[taste]
            if a == 0 and b == 0:  # Space Taste
                self.vx = 0
                self.vy = 0 
            else:
                MAX_VX = 50
                MAX_VY = 50
                if self.vx + a < MAX_VX:
                    self.vx += a
                if self.vy + b < MAX_VY:
                    self.vy += b
        else:
            super().keyPressEvent(event)

    # ----------------------------------
    # Ball bewegen
    # ----------------------------------
    def bewegen(self):

        dt = 0.020  # 20 ms

        # Position berechnen
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Fenstergrenzen beachten
        self.x = max(
            self.radius,
            min(self.width() - self.radius, self.x)
        )

        self.y = max(
            self.radius,
            min(self.height() - self.radius, self.y)
        )

        # Neuzeichnung anfordern
        self.update()

    # ----------------------------------
    # Ball zeichnen
    # ----------------------------------
    def paintEvent(self, event):

        painter = QPainter(self)

        # Hintergrund
        painter.fillRect(
            self.rect(),
            QColor("white")
        )

        # Roter Ball
        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        painter.setBrush(QColor("red"))
        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(
            int(self.x - self.radius),
            int(self.y - self.radius),
            2 * self.radius,
            2 * self.radius
        )

        painter.end()


# ----------------------------------
# Hauptprogramm
# ----------------------------------
if __name__ == "__main__":

    app = QApplication(sys.argv)

    fenster = BallFenster()
    fenster.show()
    fenster.setFocus()

    sys.exit(app.exec())
