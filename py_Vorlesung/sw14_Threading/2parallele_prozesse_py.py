import threading

def kamera_thread():
    while True:
        # Kamera auslesen
        print("Kamera läuft")
        # Hier pyrealsense2 oder OpenCV einbauen

def roboter_thread():
    while True:
        # Roboter steuern
        print("Roboter bewegt sich")
        # Hier z. B. RoboDK/ROS2-Ansteuerung implementieren

# Threads definieren und starten
t1 = threading.Thread(target=kamera_thread)
t2 = threading.Thread(target=roboter_thread)
t1.start()
t2.start()
# Optional: t1.join(), t2.join() für das Blockieren des Hauptprozesses
