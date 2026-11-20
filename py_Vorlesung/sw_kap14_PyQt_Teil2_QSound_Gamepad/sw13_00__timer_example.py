
import sys
from PyQt6.QtCore import QTimer, QObject
from PyQt6.QtWidgets import QApplication


class TimerExample(QObject):

    def __init__(self):
        super().__init__()

        self.x = 0

        # Timer erzeugen
        self.timer = QTimer(self)

        # Signal mit Methode verbinden
        self.timer.timeout.connect(self.bewegen)

        # Timer starten (alle 500 ms)
        self.timer.start(500)

    def bewegen(self):
        self.x += 5
        print(self.x)


app = QApplication(sys.argv)
te = TimerExample()
sys.exit(app.exec())
