import sys
from PySide6.QtWidgets import QApplication, QLabel   #ggf.  python -m pip install pyside6 

# Erstelle die Qt-Anwendung
app = QApplication(sys.argv)

# Erstelle ein Text-Label mit "Hello World"
label = QLabel("Hello World!")

# Zeige das Label-Fenster an
label.show()

# Starte die Ereignisschleife der Anwendung
app.exec()
