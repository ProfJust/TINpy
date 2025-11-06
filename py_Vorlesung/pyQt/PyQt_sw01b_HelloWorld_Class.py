# pyQt6_02_hello_world_class.py
# Hello World im OO-Style
#------------------------------------------------------------------
import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt6.QtCore import QSize    

class HelloWindow(QMainWindow):
    def __init__(self):  # Konstruktor
        QMainWindow.__init__(self)  # Konstruktor Elternklasse

        self.setMinimumSize(QSize(240, 80))    
        self.setWindowTitle("WHS - Campus Bocholt")

        # dynamische grid layout 
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   

        gridLayout = QGridLayout(self)     
        centralWidget.setLayout(gridLayout)  

        title = QLabel("Hello World from PyQt6", self)
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        gridLayout.addWidget(title, 0, 0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()  # Instanz der Klasse bilden
    mainWin.show()
    sys.exit( app.exec() )
