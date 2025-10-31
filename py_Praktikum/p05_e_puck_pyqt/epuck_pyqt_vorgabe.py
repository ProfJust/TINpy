# Tested OK by OJ 8.10.25
from controller import Robot, Motor, DistanceSensor
# ggf. py -3.12 -m pip install PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton
from PyQt6.QtCore import Qt, QTimer

TIME_STEP = 64
MAX_SPEED = 6.28  # E-Puck max. Radspeed (rad/s)

# --- Webots-Geraete initialisieren ---
robot = Robot()

# Proximity-IRs
ps_names = [f"ps{i}" for i in range(8)]
ps = []
for name in ps_names:
    s = robot.getDevice(name)
    s.enable(TIME_STEP)
    ps.append(s)

# Motoren
left_motor: Motor = robot.getDevice("left wheel motor")
right_motor: Motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# --- PyQt GUI ---
class EPuckGui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("E-Puck Teleoperation (PyQt6 + Webots)")
        self.left_speed = 0.0
       
        # UI-Elemente
        v = QVBoxLayout(self)

        # Geschwindigkeits-Slider (links / rechts)
        self.lbl_left = QLabel("Left: 0.00 rad/s")
        self.lbl_right = QLabel("Right: 0.00 rad/s")

        self.sld_left = QSlider(Qt.Orientation.Horizontal)
        s = self.sld_left
        s.setMinimum(int(-MAX_SPEED * 100))
        s.setMaximum(int(MAX_SPEED * 100))
        s.setValue(0)
        s.setSingleStep(5)

        self.sld_left.valueChanged.connect(self.on_left_changed)
        
        v.addWidget(self.lbl_left)
        v.addWidget(self.sld_left)
        
        # Stop-Button
        btn_row = QHBoxLayout()
        self.btn_stop = QPushButton("STOP")
        self.btn_stop.clicked.connect(self.stop)
        btn_row.addWidget(self.btn_stop)
        v.addLayout(btn_row)

        # Timer: Simulationsschritt + GUI-Update
        self.timer = QTimer(self)
        self.timer.setInterval(TIME_STEP)  # ms
        self.timer.timeout.connect(self.on_step)
        self.timer.start()

        # Optional: Tastatursteuerung (WASD / Pfeile)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    # --- UI-Callbacks ---
    def on_left_changed(self, val: int):
        self.left_speed = val / 100.0
        self.lbl_left.setText(f"Left: {self.left_speed:.2f} rad/s")

    
    def stop(self):
        self.sld_left.setValue(0)
        self.sld_right.setValue(0)
    

    # --- Webots-Step ---
    def on_step(self):
        # 1) Schritt ausführen; -1 => Sim beendet
        if robot.step(TIME_STEP) == -1:
            self.timer.stop()
            QApplication.quit()
            return

        # 2) Motoren setzen
        left_motor.setVelocity(self.left_speed)
        
        # 3) Sensoren auslesen & anzeigen
        

def main():
    app = QApplication([])
    gui = EPuckGui()
    gui.resize(420, 240)
    gui.show()
    app.exec()

if __name__ == "__main__":
    main()
