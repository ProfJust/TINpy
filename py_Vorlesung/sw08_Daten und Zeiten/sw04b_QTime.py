# from PyQt6.QtCore import QTime

# jetzt = QTime.currentTime()
# print(jetzt.toString("HH:mm:ss"))


from PyQt6.QtCore import QElapsedTimer
import time

timer = QElapsedTimer()
timer.start()

time.sleep(1.2)

print("Millisekunden:", timer.elapsed())

