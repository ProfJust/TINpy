import sys
import math
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton
)
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtCore import Qt, QRectF


class AdventWreathWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lit_candles = 0  # wie viele Kerzen brennen

    def set_lit_candles(self, n: int):
        self.lit_candles = max(0, min(4, n))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()
        size = min(width, height)

        cx = width / 2
        cy = height / 2

        outer_r = size * 0.4
        inner_r = size * 0.25

        # Hintergrund
        painter.fillRect(self.rect(), QColor("#1f1f1f"))

        # Adventskranz (grüner Ring)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor("#0b6b2a")))
        painter.drawEllipse(QRectF(cx - outer_r, cy - outer_r,
                                   2 * outer_r, 2 * outer_r))

        # inneren Kreis mit Hintergrundfarbe füllen, damit ein Ring entsteht
        painter.setBrush(QBrush(QColor("#1f1f1f")))
        painter.drawEllipse(QRectF(cx - inner_r, cy - inner_r,
                                   2 * inner_r, 2 * inner_r))

        # Kerzen zeichnen
        candle_height = size * 0.2
        candle_width = size * 0.08
        ring_r_for_candles = (outer_r + inner_r) / 2

        # vier Winkel für die Kerzen (in Grad, oben angeordnet)
        angles_deg = [-180, -90, 90, 120]

        for i, angle_deg in enumerate(angles_deg):
            a = math.radians(angle_deg)
            x_center = cx + ring_r_for_candles * math.cos(a)
            y_center = cy - ring_r_for_candles * math.sin(a)

            x = x_center - candle_width / 2
            y = y_center - candle_height

            # Kerzenkörper (rot)
            painter.setPen(QPen(QColor("#600000")))
            painter.setBrush(QBrush(QColor("#b00000")))
            candle_rect = QRectF(x, y, candle_width, candle_height)
            painter.drawRoundedRect(candle_rect, candle_width * 0.2, candle_width * 0.2)

            # Docht
            wick_height = candle_height * 0.08
            wick_width = candle_width * 0.12
            wick_x = x_center - wick_width / 2
            wick_y = y - wick_height * 0.8
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QBrush(QColor("#202020")))
            painter.drawRect(QRectF(wick_x, wick_y, wick_width, wick_height))

            # Flamme, wenn Kerze "brennt"
            if i < self.lit_candles:
                flame_h = candle_height * 0.18
                flame_w = candle_width * 0.4
                flame_x = x_center - flame_w / 2
                flame_y = wick_y - flame_h * 0.9

                # außen (orange)
                painter.setBrush(QBrush(QColor("#ff9900")))
                painter.drawEllipse(QRectF(flame_x, flame_y, flame_w, flame_h))

                # innen (gelb)
                inner_flame_h = flame_h * 0.6
                inner_flame_w = flame_w * 0.6
                inner_flame_x = x_center - inner_flame_w / 2
                inner_flame_y = flame_y + (flame_h - inner_flame_h) * 0.5
                painter.setBrush(QBrush(QColor("#ffff66")))
                painter.drawEllipse(QRectF(inner_flame_x, inner_flame_y,
                                           inner_flame_w, inner_flame_h))


class AdventWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Adventskranz")
        self.resize(600, 500)

        self.wreath = AdventWreathWidget()

        self.btn_next = QPushButton("Nächste Kerze anzünden")
        self.btn_reset = QPushButton("Alle Kerzen löschen")

        self.btn_next.clicked.connect(self.light_next)
        self.btn_reset.clicked.connect(self.reset_candles)

        layout = QVBoxLayout()
        layout.addWidget(self.wreath, stretch=1)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch(1)
        btn_layout.addWidget(self.btn_next)
        btn_layout.addWidget(self.btn_reset)
        btn_layout.addStretch(1)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

        # Optional: gleich die erste Kerze "anzünden"
        self.current_lit = 0
        self.update_wreath()

    def update_wreath(self):
        self.wreath.set_lit_candles(self.current_lit)

    def light_next(self):
        if self.current_lit < 4:
            self.current_lit += 1
            self.update_wreath()

    def reset_candles(self):
        self.current_lit = 0
        self.update_wreath()


def main():
    app = QApplication(sys.argv)
    window = AdventWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
