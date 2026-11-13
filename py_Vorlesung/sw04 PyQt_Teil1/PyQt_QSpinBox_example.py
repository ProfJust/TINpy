from PyQt6.QtWidgets import QApplication, QWidget, QSpinBox, QVBoxLayout

app = QApplication([])

win = QWidget()
layout = QVBoxLayout(win)

spin = QSpinBox()
layout.addWidget(spin)

win.show()
app.exec()

# Wertebereich und Startwert setzen:

spin.setMinimum(0)
spin.setMaximum(100)
spin.setValue(10)
spin.setSingleStep(5)   # Schrittweite
# Auf Wertänderung reagieren:

def on_value_changed(value: int):
    print("Neuer Wert:", value)
