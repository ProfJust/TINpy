
import sys
from pathlib import Path
import pygame

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QPixmap
from PyQt6.QtCore import Qt, QTimer


class MeinFenster(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kreis auf Rasen")
        self.setFixedSize(800, 600)

        # Rasenbild laden
        bildpfad = Path(__file__).resolve().parent / "rasen.jpg"
        self.pixmap = QPixmap(str(bildpfad))
        if self.pixmap.isNull():
            print("Bild nicht gefunden:", bildpfad)
       
        self.x = 300.0    # Kreisposition
        self.y = 200.0
        self.radius = 25
        self.geschwindigkeit = 250
       
        pygame.init()     # Gamepad initialisieren
        pygame.joystick.init()
        self.gamepad = None
        if pygame.joystick.get_count() > 0:
            self.gamepad = pygame.joystick.Joystick(0)
            self.gamepad.init()
            print("Gamepad:", self.gamepad.get_name())
        else:
            print("Kein Gamepad gefunden!")
    
        self.timer = QTimer(self)    # Timer
        self.timer.timeout.connect(self.update_position)
        self.timer.start(20)

    # ----------------------------------------
    # Hintergrund und Kreis zeichnen
    # ----------------------------------------
    def paintEvent(self, event):
        painter = QPainter(self)
        if not self.pixmap.isNull():    # 1. pixmap als Hintergrund
            painter.drawPixmap(
                self.rect(),
                self.pixmap
            )
        else:
            painter.fillRect(self.rect(), QColor("green"))

        painter.setBrush(QColor("red"))  # 2. Roten Kreis darüber zeichnen
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(
            int(self.x - self.radius),
            int(self.y - self.radius),
            2 * self.radius,
            2 * self.radius
        )
        painter.end()

    # ----------------------------------------
    # Gamepad-Steuerung
    # ----------------------------------------
    def update_position(self):

        if self.gamepad is None:
            return

        pygame.event.pump()

        achse_x = self.gamepad.get_axis(0)
        achse_y = self.gamepad.get_axis(1)

        # Totzone
        if abs(achse_x) < 0.15:
            achse_x = 0.0

        if abs(achse_y) < 0.15:
            achse_y = 0.0

        dt = 0.020

        self.x += achse_x * self.geschwindigkeit * dt
        self.y += achse_y * self.geschwindigkeit * dt

        # Fenstergrenzen
        self.x = max(self.radius,
                     min(self.width() - self.radius, self.x))

        self.y = max(self.radius,
                     min(self.height() - self.radius, self.y))

        self.update()

    def closeEvent(self, event):
        self.timer.stop()
        pygame.quit()
        event.accept()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    fenster = MeinFenster()
    fenster.show()

    sys.exit(app.exec())


from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap

self.lbl1 = QLabel(self)
self.lbl1.setGeometry(100, 100, 196, 442)

pix = QPixmap("Streicholz.PNG")
self.lbl1.setPixmap(pix)

self.lbl1.setDisabled(True)  # Ausgrauen
