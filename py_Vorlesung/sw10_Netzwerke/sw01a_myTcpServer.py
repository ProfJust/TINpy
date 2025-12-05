import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress


class MyTcpServer(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- UI / Fenster ---
        self.setWindowTitle("Python TCP Server")
        self.setGeometry(100, 100, 500, 150)

        # Label zur Ausgabe
        self.lbl = QLabel(self)
        self.lbl.setGeometry(10, 40, 480, 40)
        self.lbl.setText("Label zur Ausgabe von Text")

        # --- TCP Server ---
        self.server = QTcpServer(self)
        self.server.newConnection.connect(self.new_connection_slot)

        # Starte Server auf Port 80 
        # Unter Linux/Windows/macOS darf Port <1024 nur mit Admin/Root 
        # geöffnet werden. => Any
        # if not self.server.listen(QHostAddress.SpecialAddress.Any, 80):
        if not self.server.listen(QHostAddress.SpecialAddress.Any, 5000):     
            self.lbl.setText("Server konnte nicht gestartet werden!")
        else:
            self.lbl.setText("Server erfolgreich gestartet!")

    # --- Client-Verbindung behandeln ---
    def new_connection_slot(self):
        socket: QTcpSocket = self.server.nextPendingConnection()

        # Warte bis Daten verfügbar
        if not socket.waitForReadyRead(3000):
            self.lbl.setText("Timeout – keine Daten erhalten")
            socket.close()
            return

        # Zeile lesen (wie readLine in C++)
        data = socket.readLine().data().decode("utf-8")
        self.lbl.setText(f"Client fragt: {data}")

        # Antwortlogik
        if data == "Hallo Server, wie ist das Wetter heute? \r\n":
            answer = "Server sendet: 25 Grad Celsius, sonnig, 18kn Wind \r\n"
        else:
            answer = "Server sendet: Hallo Client, was moechtest Du wissen? \r\n"

        # Antwort senden
        socket.write(answer.encode("utf-8"))
        socket.flush()
        socket.waitForBytesWritten(3000)
        socket.close()


# --- main() ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyTcpServer()
    window.show()
    sys.exit(app.exec())
