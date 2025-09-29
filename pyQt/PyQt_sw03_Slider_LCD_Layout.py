#!/usr/bin/env python3
# ---------------------------------------------------------------------
# pyqt_sw07_LCD_Slider.py
# Beispiel fuer Signal Slot Konzept
# ---------------------------------------------------------------------
# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import (QWidget, QSlider,
                             QLCDNumber, QApplication, QPushButton)
from PyQt6.QtCore import Qt
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # --- Slider erstellen -----
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

    # --- Die beiden Slot-Methoden
    def plus(self):
        wert = self.mySlider.value()  # Slider Wert holen
        wert = wert+1
        self.mySlider.setValue(wert)  # Slider Wert setzen

    def minus(self):
        wert = self.mySlider.value()
        wert = wert-1
        self.mySlider.setValue(wert)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
