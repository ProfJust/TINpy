import sys
import os

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import QUrl
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest


class GetPicFromWeb(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Größe des Main-Windows setzen (wie im C++-Code)
        self.resize(1020, 860)
        self.setWindowTitle("GetPicFromWeb – PyQt6")

        # --- Button: Connect and get picture! ---
        self.myButton = QPushButton(self)
        self.myButton.setGeometry(10, 10, 160, 40)  # x, y, w, h
        self.myButton.setText(" Connect and get picture! ")

        # --- Button: Save picture ---
        self.saveButton = QPushButton(self)
        self.saveButton.setGeometry(200, 10, 160, 40)
        self.saveButton.setText(" Not enabled yet ")
        self.saveButton.setEnabled(False)

        # --- Label für Bild ---
        self.myLabel = QLabel(" Label fuer Bild von Webcam ", self)
        self.myLabel.setGeometry(10, 50, 1000, 800)
        self.myLabel.setFont(QFont("Helvetica", 10))
        self.myLabel.setScaledContents(True)  # Bild an Labelgröße anpassen

        # --- Netzwerk-Komponenten ---
        self.nam = QNetworkAccessManager(self)
        self.nam.finished.connect(self.downloadFinishedEvent)

        self.reply = None
        self.pix = None

        # Zähler für Dateinamen
        self.image_counter = 1

        # URL wie im C++-Code
        self.url = QUrl(
            "https://webcam.bergbauernmuseum.de/typo3/fileadmin/bbm/webcam/bbm.jpg"
        )

        # Signale mit Slots verbinden
        self.myButton.clicked.connect(self.on_pushButton_clicked)
        self.saveButton.clicked.connect(self.on_saveButton_clicked)

        # Arbeitsverzeichnis setzen
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)

    # --- Event Callback, wenn Download fertig ---
    def downloadFinishedEvent(self, reply):
        # QPixmap aus den empfangenen Bytes erzeugen
        self.pix = QPixmap()
        data = reply.readAll()
        if not self.pix.loadFromData(data):
            self.myLabel.setText("Fehler beim Laden des Bildes!")
            self.saveButton.setEnabled(False)
            self.saveButton.setText(" Not enabled yet ")
            return

        # Pixmap auf Label setzen
        self.myLabel.setPixmap(self.pix)

        # Save erst aktivieren, wenn ein Bild vorhanden ist
        self.saveButton.setText(" Save picture to file ")
        self.saveButton.setEnabled(True)

    # --- Button: Bild von Web holen ---
    def on_pushButton_clicked(self):
        # Request an URL senden
        request = QNetworkRequest(self.url)
        self.reply = self.nam.get(request)
        self.myLabel.setText("Lade Bild von Webcam ...")
        self.saveButton.setEnabled(False)
        self.saveButton.setText(" Not enabled yet ")

    # --- Button: Bild speichern ---
    def on_saveButton_clicked(self):
        if self.pix is None:
            self.myLabel.setText("Kein Bild zum Speichern vorhanden!")
            return

        # Dateinamen zusammenbauen: myFile1.png, myFile2.png, ...
        file_name = f"myFile{self.image_counter}.png"
        self.image_counter += 1

        # Bild speichern
        if self.pix.save(file_name, "PNG"):
            self.myLabel.setText(f"Bild gespeichert als {file_name}")
        else:
            self.myLabel.setText("Fehler beim Speichern des Bildes!")

        # Save-Button deaktivieren bis zum nächsten Download
        self.saveButton.setEnabled(False)
        self.saveButton.setText(" Not enabled yet ")


def main():
    app = QApplication(sys.argv)
    window = GetPicFromWeb()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
