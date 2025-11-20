import sys
import random  # Für Zufallszahlen
import time
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QSpinBox, QVBoxLayout, QHBoxLayout, QGridLayout
)
MIN_HOLZ = 16; MAX_HOLZ = 25  # Maximale Anzahl der Hölzer

class NimmspielQt(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nimmspiel Qt (PyQt6)")
        # Anzahl der Hölzer per Zufall initieren
        self.wHoelzer = random.randint(MIN_HOLZ, MAX_HOLZ)  
        self.Mensch_ist_am_Zug = True
        # Widgets
        self.infoLbl = QLabel("Nimm 1 bis 3 Hölzer. Wer das letzte nimmt, verliert.")
        self.zugLbl = QLabel("  ")
        self.compLbl = QLabel("Computer: noch kein Zug.")
        self.spinBox = QSpinBox()
        self.spinBox.setRange(1, 3)
        self.spinBox.setValue(3)
        self.btn = QPushButton("Zug ausführen")

        # Hölzer-Anzeige aus Labeln
        self.holz = [QLabel("🟫") for _ in range(MAX_HOLZ)]
        for HolzLbl in self.holz:
            HolzLbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            HolzLbl.setStyleSheet("font-size: 20px;")

        # Layouts
        central = QWidget()
        self.setCentralWidget(central)

        topLayout = QVBoxLayout()
        topLayout.addWidget(self.infoLbl)
        topLayout.addWidget(self.zugLbl)
        topLayout.addWidget(self.compLbl)

        controlLayout = QHBoxLayout()
        controlLayout.addWidget(QLabel("Dein Zug:"))
        controlLayout.addWidget(self.spinBox)
        controlLayout.addWidget(self.btn)
        controlLayout.addStretch(1)

        # Grid für Hölzer (z. B. 5 x 5)
        grid = QGridLayout()
        rows, cols = 3, 10
        idx = 0
        for r in range(rows):
            for c in range(cols):
                grid.addWidget(self.holz[idx], r, c)
                idx += 1
                if idx >= self.wHoelzer: break # Vermeide List Out Of Range

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(controlLayout)
        mainLayout.addLayout(grid)

        central.setLayout(mainLayout)
        # Signale
        self.btn.clicked.connect(self.myBtnSlot)
        # Initial anzeigen
        self.gebeAnzHoelzerAus()

    # Slots
    def myBtnSlot(self):
        self.Mensch_ist_am_Zug = True
        self.wHoelzer -= self.spinBox.value()    
        if self.pruef_ob_gewonnen() != True:
            self.Mensch_ist_am_Zug = False
            self.holeComputerZug(self.wHoelzer)            
        # --- für die nächste Runde ---
        self.gebeAnzHoelzerAus()
        self.spinBox.setRange(1, min(3, self.wHoelzer))

    def holeComputerZug(self, verbleibend: int):
        # Einfache (schlagende) Nim-Strategie: n % 4 auf 1 setzen, wenn möglich
        if verbleibend <= 0:
            return
        if verbleibend % 4 == 0:
            comp_take = 3
        elif verbleibend % 4 == 3:
            comp_take = 2
        elif verbleibend % 4 == 2:
            comp_take = 1
        else:
            # Wenn optimaler Zug nicht möglich, zufällig 1..verbleibend)
            comp_take = min(random.randint(1, verbleibend), 3)
    
        self.wHoelzer -= comp_take
        self.compLbl.setText(f"Computer nimmt {comp_take}.") 
                
    def gebeAnzHoelzerAus(self):
        # Sichtbarkeit der Hölzer entsprechend wHoelzer
        for i, h in enumerate(self.holz):
            h.setVisible(i < self.wHoelzer)
        self.zugLbl.setText(f"Hölzer übrig: {self.wHoelzer}")
        

    def pruef_ob_gewonnen(self):
        if self.wHoelzer == 1:
            self.infoLbl.setText("Computer musste das letzte Holz nehmen. Du gewinnst!")
            self.btn.setEnabled(False)
            self.spinBox.setEnabled(False)
            return True
        if self.wHoelzer == 0:
            self.infoLbl.setText("Du musstest das letzte Holz nehmen. Du verlierst!")
            self.btn.setEnabled(False)
            self.spinBox.setEnabled(False)
            return False
        
        

def main():
    app = QApplication(sys.argv)
    w = NimmspielQt()
    w.resize(540, 420)
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
