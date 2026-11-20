import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl


class MeinFenster(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("WAV Player")
        self.resize(300, 150)

        # Verzeichnis des Python-Skripts
        ordner = Path(__file__).resolve().parent

        # WAV-Datei im gleichen Verzeichnis
        datei = ordner / "yeah.wav"

        print("Datei:", datei)
        print("Existiert:", datei.is_file())

        # Sound laden
        self.sound = QSoundEffect(self)
        self.sound.setSource(QUrl.fromLocalFile(str(datei)))
        self.sound.setVolume(0.8)

        # Button
        self.button = QPushButton("Sound abspielen")
        self.button.clicked.connect(self.sound.play)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    fenster = MeinFenster()
    fenster.show()

    sys.exit(app.exec())