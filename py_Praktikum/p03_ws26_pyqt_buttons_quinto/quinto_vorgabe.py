"""Praktikum 4: Quinto mit PyQt6 (Python 3.12)."""
import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox

N = 4  # Erweiterung: N = 5
BLAU = False
ROT = True

class MyButton(QPushButton):
    """QPushButton mit Spielfeldkoordinaten und Farbzustand."""
    def __init__(self, reihe, spalte, parent=None):
        super().__init__(parent)
        self.btnReihe = reihe
        self.btnSpalte = spalte
        self.owner = BLAU
        self.setFixedSize(80, 80)
        self.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border: 1px solid black;
                border-radius: 0px;
            }"""
        )

class Quinto(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TIN – PyQt6 Quinto")
        self.numbOfKlicks = 0
        self.spielFeld = []
        self.spielzugLbl = QLabel("Quinto: Alle Felder rot färben!")
        self.zaehlerLbl = QLabel("Anzahl Klicks: 0")
        # Hier weitere Buttons ergänzen 

        # Hier die Buttons mit den Callback-Methoden verbinden
        # z.B. restartClicked()

        hauptlayout = QHBoxLayout(self)
        grid = QGridLayout()
        grid.setSpacing(0)
        grid.setContentsMargins(0, 0, 0, 0)
        # Reihen nicht vertikal auseinanderziehen
        grid.setRowStretch(N, 1)
        grid.setContentsMargins(0, 0, 0, 0)
        for r in range(N):
            zeile = []
            for s in range(N):
                btn = MyButton(r, s, self)
                btn.clicked.connect(lambda checked=False, b=btn: self.myButtonClicked(b))
                grid.addWidget(btn, r, s)
                zeile.append(btn)
            self.spielFeld.append(zeile)
        hauptlayout.addLayout(grid, 4)
        seite = QVBoxLayout()
        seite.addWidget(self.spielzugLbl)
        seite.addWidget(self.zaehlerLbl)
        seite.addStretch()
        # Ergänze Widgets hier
        hauptlayout.addLayout(seite, 2)
        self.resize(680, 440)

    def toggleButton(self, r, s):
        """Farbe und Zustand eines gültigen Feldes umschalten."""
        btn = self.spielFeld[r][s]
        btn.owner = not btn.owner
        farbe = "red" if btn.owner == ROT else "blue"
        
        btn.setStyleSheet(
            f"background-color: {farbe}; "
             "border: 1px solid black; "
             "border-radius: 0px;"
        )
        

    def myButtonClicked(self, btn):
        r, s = btn.btnReihe, btn.btnSpalte
        self.toggleButton(r, s)  # angeklicktes Feld (bereits implementiert)
        # TODO a): Nachbarn oben, unten, links und rechts toggeln.
        # Beachten Sie die Spielfeldgrenzen (0 <= Index < N).
        # TODO c): Klickzähler erhöhen und zaehlerLbl aktualisieren.
        self.spielzugLbl.setText(f"Feld ({r}, {s}) geklickt")
        # TODO b): checkGameOver() aufrufen; bei Gewinn Meldung ausgeben
        # und Spielfeldbuttons deaktivieren.
        # TODO d): optional yeah.wav abspielen (PyQt6.QtMultimedia).

    def checkGameOver(self):
        # TODO b): True zurückgeben, wenn alle Felder ROT sind.
        return False

    def restartClicked(self):
        # TODO e): Alle Felder blau setzen und wieder aktivieren,
        # Klickzähler auf 0 setzen und Labels zurücksetzen.
        pass

    def spieleGewinnsound(self):
        """Spielt yeah.wav ab, falls Datei und Multimedia verfügbar sind."""
        wav = Path(__file__).with_name("yeah.wav")
        if not wav.is_file():
            return
        try:
            from PyQt6.QtCore import QUrl
            from PyQt6.QtMultimedia import QSoundEffect
            self.sound = QSoundEffect(self)
            self.sound.setSource(QUrl.fromLocalFile(str(wav)))
            self.sound.setVolume(0.7)
            self.sound.play()
        except ImportError:
            print("Hinweis: PyQt6.QtMultimedia ist nicht verfügbar.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenster = Quinto()
    fenster.show()
    sys.exit(app.exec())
