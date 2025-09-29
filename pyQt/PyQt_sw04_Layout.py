from PyQt6.QtWidgets import (QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout)  # Add VBoxLayout
from PyQt6.QtCore import Qt

import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        Button1 = QPushButton('PyQt')
        Button2 = QPushButton('Layout')
        Button3 = QPushButton('Management')
        Button4 = QPushButton(' Qt06')

        vbox = QVBoxLayout()
        vbox.addWidget(Button1)
        vbox.addWidget(Button2)
        
        hbox = QHBoxLayout()
        hbox.addWidget(Button3)
        hbox.addWidget(Button4)
        vbox.addLayout(hbox)  # ADD LAYOUT
 
        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PyQt5 Layout')
        self.show()  


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
 

