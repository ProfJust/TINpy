# ---------------------------------------------------------------------
# PyQt_sw03_Slider_LCD.py
# Beispiel fuer Signal Slot Konzept
# ---------------------------------------------------------------------
from PyQt6.QtWidgets import (
    QWidget, QSlider, QLCDNumber,
    QApplication, QPushButton, QHBoxLayout, QVBoxLayout
)
from PyQt6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.mySlider = QSlider(Qt.Orientation.Horizontal, self)
        self.mySlider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.mySlider.setGeometry(30, 40, 180, 30)  # x,y,w,h
        self.mySlider.setValue(20)

        # --- LCD konstruieren -----
        self.myLcd = QLCDNumber(2, self)
        self.myLcd.setGeometry(60, 100, 80, 50)  # x,y,w,h
        self.myLcd.display(20)

        # Verbinden des Signals valueChanged
        # mit der Slot-Funktion myLcd.display
        self.mySlider.valueChanged[int].connect(self.myLcd.display)

        # --- zwei PushButtons
        self.myPBmore = QPushButton(self)
        self.myPBmore.setText('>')
        self.myPBmore.setGeometry(0, 0, 40, 40)   # x,y,w,h
        self.myPBmore.clicked.connect(self.plus)

        self.myPBless = QPushButton(self)
        self.myPBless.setText('<')
        self.myPBless.setGeometry(180, 0, 40, 40)  # x,y,w,h
        self.myPBless.clicked.connect(self.minus)

        # --- Window konfigurieren
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('PyQt6 - Slider LCD')
        self.show()

    # --- Slot Methoden mit Wertebegrenzung ---
    def plus(self):
        wert = self.mySlider.value()
        if wert < self.mySlider.maximum():
            self.mySlider.setValue(wert + 1)

    def minus(self):
        wert = self.mySlider.value()
        if wert > self.mySlider.minimum():
            self.mySlider.setValue(wert - 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
