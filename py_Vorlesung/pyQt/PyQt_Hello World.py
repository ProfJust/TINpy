# PyQt_Hello World.py
#---------------------------------------
# Erstellt ein erstes Fenster mit PyQt6
# -----------------------------------------
# OJ am 29.09.2025
# ggf. notwendig  >pip install PyQt6
# ERROR: Activate.ps1" kann nicht geladen werden,
#  da die Ausführung von Skripts auf diesem System deaktiviert ist. 
# ==>>
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser


from PyQt6.QtWidgets import QApplication, QWidget, QLabel

# Only needed for access to command line arguments
import sys

def window():
   app = QApplication(sys.argv)

   # Create a Qt widget, which will be our window.
   w = QWidget() 
   # Set Size and Title of Window
   w.setGeometry(100,100,200,50)
   w.setWindowTitle("PyQt - Version Qt6")
   # Create a Label on that window
   label = QLabel(w)
   label.setText("Hello World!")  
   # Where to move the label
   label.move(50,20)
  
   # IMPORTANT!!!!! Windows are hidden by default.
   w.show()
   # Start the event loop.
   app.exec()
   
if __name__ == '__main__':
   window()
