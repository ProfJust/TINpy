import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class MeinFenster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 KeyEvent")
        self.setFixedSize(400, 300)
        # Position des Kreises
        self.x = 150
        self.y = 100
        # Tastaturfokus setzen
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor("red"))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(self.x, self.y, 50, 50)
        painter.end()

    def keyPressEvent(self, event):
        # Welche Taste wurde gedrückt?
        taste = event.key()
        if taste == Qt.Key.Key_Up:
            self.y -= 10
        elif taste == Qt.Key.Key_Down:
            self.y += 10
        elif taste == Qt.Key.Key_Left:
            self.x -= 10
        elif taste == Qt.Key.Key_Right:
            self.x += 10
        elif taste == Qt.Key.Key_Escape:
            self.close()
            return
        else:
            super().keyPressEvent(event)
            return
        # Fenster neu zeichnen
        self.update()
        

    def keyReleaseEvent(self, event):
        if not event.isAutoRepeat():
            print("Taste losgelassen:", event.key())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenster = MeinFenster()
    fenster.show()
    sys.exit(app.exec())