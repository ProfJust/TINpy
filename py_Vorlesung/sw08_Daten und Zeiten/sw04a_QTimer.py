from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtCore import QTimer
import sys

class Window(QLabel):
    def __init__(self):
        super().__init__("Warte...")
        self.counter = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)  # alle 1.0 Sekunden

    def update_label(self):
        self.counter += 1
        self.setText(f"Sekunden: {self.counter}")

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()

# from PyQt6.QtCore import QTimer

# def starte_nach_2s():
#     print("2 Sekunden sind vorbei!")

# QTimer.singleShot(2000, starte_nach_2s)

# self.timer.stop()