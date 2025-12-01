import sys
import math
import random
import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel
)
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtCore import Qt, QRectF, QTimer


def advent_sundays(year: int):
    """Gibt die vier Adventssonntage (1.–4. Advent) als datetime.date-Tupel zurück."""
    christmas = datetime.date(year, 12, 25)

    # weekday(): Montag = 0, ..., Sonntag = 6
    weekday = christmas.weekday()

    # Sonntag vor (oder an) Weihnachten bestimmen
    days_back_to_sunday = (weekday + 1) % 7
    fourth_advent = christmas - datetime.timedelta(days=days_back_to_sunday)

    third_advent = fourth_advent - datetime.timedelta(days=7)
    second_advent = third_advent - datetime.timedelta(days=7)
    first_advent = second_advent - datetime.timedelta(days=7)

    return (first_advent, second_advent, third_advent, fourth_advent)


def get_advent_status(day: datetime.date):
    """
    Bestimmt:
      - wie viele Adventssonntage (0–4) schon vorbei/inkl. heute sind
      - ob heute ein Adventssonntag ist (1–4 oder 0)
      - die vier Advents-Daten

    Rückgabe:
      candles_lit, today_index, advent_dates
      candles_lit: 0–4 (Anzahl brennender Kerzen)
      today_index: 0,1,2,3,4 (0 = kein Adventssonntag, sonst Nummer)
      advent_dates: Tuple mit den 4 Adventssonntagen
    """
    year = day.year
    advent_dates = advent_sundays(year)

    # wie viele Adventssonntage liegen vor oder auf heute?
    candles_lit = sum(1 for d in advent_dates if d <= day)

    # ist heute ein Adventssonntag?
    today_index = 0
    for i, d in enumerate(advent_dates, start=1):
        if d == day:
            today_index = i
            break

    return candles_lit, today_index, advent_dates


class AdventWreathWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lit_candles = 0  # wie viele Kerzen brennen
        self.flame_offsets = [0, 0, 0, 0]  # Flacker-Animation

        # Timer für das Flackern
        self.timer = QTimer(self)
        self.timer.setInterval(120)  # alle 120 ms neue Flammenform
        self.timer.timeout.connect(self.update_flames)
        self.timer.start()

    def update_flames(self):
        # Zufällige Flacker-Werte für jede Kerze
        for i in range(4):
            self.flame_offsets[i] = random.uniform(-4, 4)
        self.update()

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
        cy = height / 2 + size * 0.1  # Ring leicht nach unten verschieben

        # *** Flacher Adventskranz: Ellipse statt Kreis ***
        outer_rx = size * 0.45
        outer_ry = size * 0.20    # flach!
        inner_rx = size * 0.30
        inner_ry = size * 0.12

        # Hintergrund dunkel
        painter.fillRect(self.rect(), QColor("#1f1f1f"))

        # Äußere Ellipse (grün)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor("#0b6b2a")))
        painter.drawEllipse(QRectF(cx - outer_rx, cy - outer_ry,
                                   2 * outer_rx, 2 * outer_ry))

        # Innere Ellipse (ausgeschnitten)
        painter.setBrush(QBrush(QColor("#1f1f1f")))
        painter.drawEllipse(QRectF(cx - inner_rx, cy - inner_ry,
                                   2 * inner_rx, 2 * inner_ry))

        # Kerzenparameter
        candle_height = size * 0.28
        candle_width = size * 0.08

        # Abstand für Kerzen (auf dem flachen Kranz)
        ring_rx = (outer_rx + inner_rx) / 2
        ring_ry = (outer_ry + inner_ry) / 2

        #angles_deg = [-70, -30, 10, 50]
        angles_deg = [-180, -110, 10, 70]

        for i, angle_deg in enumerate(angles_deg):

            a = math.radians(angle_deg)
            x_center = cx + ring_rx * math.cos(a)
            y_center = cy - ring_ry * math.sin(a)

            x = x_center - candle_width / 2
            y = y_center - candle_height

            # Kerzenkörper
            painter.setPen(QPen(QColor("#600000")))
            painter.setBrush(QBrush(QColor("#b00000")))
            candle_rect = QRectF(x, y, candle_width, candle_height)
            painter.drawRoundedRect(candle_rect, candle_width * 0.2, candle_width * 0.2)

            # Docht
            wick_h = candle_height * 0.07
            wick_w = candle_width * 0.15
            wick_x = x_center - wick_w / 2
            wick_y = y - wick_h * 1.1

            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QBrush(QColor("#202020")))
            painter.drawRect(QRectF(wick_x, wick_y, wick_w, wick_h))

            # Flamme mit Animation
            if i < self.lit_candles:
                flicker = self.flame_offsets[i]

                flame_h = candle_height * 0.20 + flicker
                flame_w = candle_width * 0.40 + flicker / 2

                # Mindestgrößen, damit die Flamme nicht "verschwindet"
                flame_h = max(flame_h, candle_height * 0.12)
                flame_w = max(flame_w, candle_width * 0.25)

                flame_x = x_center - flame_w / 2
                flame_y = wick_y - flame_h * 0.9

                # Außenflamme (orange)
                painter.setBrush(QBrush(QColor("#ff9900")))
                painter.drawEllipse(QRectF(flame_x, flame_y, flame_w, flame_h))

                # Innenflamme (gelb)
                inner_h = flame_h * 0.6
                inner_w = flame_w * 0.6
                inner_x = x_center - inner_w / 2
                inner_y = flame_y + (flame_h - inner_h) * 0.5

                painter.setBrush(QBrush(QColor("#ffff66")))
                painter.drawEllipse(QRectF(inner_x, inner_y, inner_w, inner_h))


class AdventWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Adventskranz")
        self.resize(650, 540)

        # Heutiges Datum + Adventsstatus bestimmen
        self.today = datetime.date.today()
        self.candles_lit, self.today_index, self.advent_dates = \
            get_advent_status(self.today)

        # GUI-Elemente
        self.info_label = QLabel()
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setStyleSheet("color: white; font-size: 16px;")

        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_label.setStyleSheet("color: #dddddd; font-size: 12px;")

        self.wreath = AdventWreathWidget()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.date_label)
        layout.addWidget(self.wreath, stretch=1)

        self.setLayout(layout)

        # Anzahl brennender Kerzen = Anzahl vergangener Adventssonntage
        self.wreath.set_lit_candles(self.candles_lit)
        self.update_labels()

    def update_labels(self):
        today_str = self.today.strftime("%d.%m.%Y")

        if self.candles_lit == 0:
            first_advent = self.advent_dates[0]
            first_str = first_advent.strftime("%d.%m.%Y")
            text = f"Heute ist noch kein Advent. 1. Advent am {first_str}."
        elif self.candles_lit < 4:
            text = f"Wir sind in der Adventszeit. {self.candles_lit} Kerze(n) brennen."
            if self.today_index in (1, 2, 3, 4):
                text = f"Heute ist der {self.today_index}. Advent – {self.candles_lit} Kerze(n) brennen."
        else:
            # alle vier Adventssonntage vorbei
            if self.today_index == 4:
                text = "Heute ist der 4. Advent – alle vier Kerzen brennen."
            else:
                text = "Alle vier Adventssonntage liegen hinter uns – alle vier Kerzen brennen."

        self.info_label.setText(text)
        self.date_label.setText(f"Heutiges Datum: {today_str}")


def main():
    app = QApplication(sys.argv)
    window = AdventWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
