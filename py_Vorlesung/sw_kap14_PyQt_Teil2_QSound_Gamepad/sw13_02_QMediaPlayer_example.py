import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout
)
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl


class MeinFenster(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("WAV/MP3 Player")
        self.resize(300, 200)

        # Audioausgabe
        self.audio = QAudioOutput()
        self.audio.setVolume(0.8)

        # MediaPlayer
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio)
        # self.player.setSource(QUrl.fromLocalFile("sound.wav"))
        # Freies Audiofile
        # https://pixabay.com/de/sound-effects/musical-timbo-drumline-loop-103bpm-171091/
        self.player.setSource(
                QUrl.fromLocalFile(
                    r"C:\sciebo_robotik\_TINpy\_git_WS26_nov\TINpy\py_Vorlesung\sw_kap13_QSound\kamhunt-timbo-drumline-loop-103bpm-171091.mp3"
                )
        )

        # Buttons
        layout = QVBoxLayout(self)

        start = QPushButton("Start")
        pause = QPushButton("Pause")
        stopp = QPushButton("Stopp")

        start.clicked.connect(self.player.play)
        pause.clicked.connect(self.player.pause)
        stopp.clicked.connect(self.player.stop)

        layout.addWidget(start)
        layout.addWidget(pause)
        layout.addWidget(stopp)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    fenster = MeinFenster()
    fenster.show()

    sys.exit(app.exec())