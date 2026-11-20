
import sys
import pygame

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QTimer


class MeinFenster(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Gamepad-Steuerung")
        self.setFixedSize(600, 400)

        # Kreisposition
        self.x = 300.0
        self.y = 200.0
        self.radius = 25

        # Geschwindigkeit in Pixel/Sekunde
        self.geschwindigkeit = 250

        # Pygame initialisieren
        pygame.init()
        pygame.joystick.init()

        # Gamepad suchen
        self.gamepad = None

        if pygame.joystick.get_count() > 0:
            self.gamepad = pygame.joystick.Joystick(0)
            self.gamepad.init()
            print("Gamepad:", self.gamepad.get_name())
        else:
            print("Kein Gamepad gefunden!")

        # Timer: 20 ms = 50 Aktualisierungen/s
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(20)

    # ----------------------------------------
    # Kreis zeichnen
    # ----------------------------------------
    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setBrush(QColor("red"))
        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(
            int(self.x - self.radius),
            int(self.y - self.radius),
            2 * self.radius,
            2 * self.radius
        )

        painter.end()

    # ----------------------------------------
    # Gamepad auslesen und Kreis bewegen
    # ----------------------------------------
    def update_position(self):   # Gamepad auslesen und Kreis bewegen
        if self.gamepad is None:
            return
        
        pygame.event.pump()                  # Pygame-Events aktualisieren
        achse_x = self.gamepad.get_axis(0)   # Linken Analogstick auslesen
        achse_y = self.gamepad.get_axis(1)
       
        if abs(achse_x) < 0.15:   # Totzone
            achse_x = 0.0
        if abs(achse_y) < 0.15:
            achse_y = 0.0
        
        dt = 0.020            # Zeitintervall 20 ms
        
        self.x += achse_x * self.geschwindigkeit * dt     # Neue Position
        self.y += achse_y * self.geschwindigkeit * dt
        
        self.x = max(     # Fenstergrenzen beachten
            self.radius, 
            min(self.width() - self.radius, self.x)
        )
        self.y = max(
            self.radius,
            min(self.height() - self.radius, self.y)
        )
        self.update()   # Neuzeichnung anfordern

    # ----------------------------------------
    # Fenster schließen
    # ----------------------------------------
    def closeEvent(self, event):

        self.timer.stop()
        pygame.quit()

        event.accept()


# --------------------------------------------
# Hauptprogramm
# --------------------------------------------
if __name__ == "__main__":

    app = QApplication(sys.argv)

    fenster = MeinFenster()
    fenster.show()

    sys.exit(app.exec())
