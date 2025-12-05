import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtNetwork import QTcpSocket
#from PyQt6.QtCore import QIODevice


class MyTcpClient(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- UI ---
        self.setWindowTitle("Python TCP Client")
        self.setGeometry(200, 200, 500, 150)

        self.lbl = QLabel(self)
        self.lbl.setText("Label zur Ausgabe von Text")
        self.lbl.setGeometry(10, 40, 480, 40)

        # Starte die Verbindung wie im C++-Konstruktor
        self.send_request()

    # --- Anfrage an den Server senden ---
    def send_request(self):
        self.socket = QTcpSocket(self)

        # Mit localhost verbinden (port ggf. anpassen!)
        self.socket.connectToHost("127.0.0.1", 5000)

        # Warten ob Verbindung aufgebaut wird
        if not self.socket.waitForConnected(3000):
            self.lbl.setText("Keine Verbindung!")
            return

        self.lbl.setText("Verbindung steht!")

        # Anfrage senden (exakt wie im C++-Code)
        request = "Hallo Server, wie ist das Wetter heute? \r\n"
        self.socket.write(request.encode())
        self.socket.waitForBytesWritten(1000)

        # Auf Antwort warten
        if self.socket.waitForReadyRead(3000):
            reply = self.socket.readAll().data().decode("utf-8")
            self.lbl.setText("Antwort: " + reply)
        else:
            self.lbl.setText("Keine Antwort vom Server")

        self.socket.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyTcpClient()
    window.show()
    sys.exit(app.exec())
