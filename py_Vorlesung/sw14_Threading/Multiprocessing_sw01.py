import multiprocessing
import time


def kamera_task():
    # Kamera auslesen
    while True:
        print("Bild von Kamera holen")
        time.sleep(1)
  

def roboter_task():
    # Roboter steuern
    while True:
        print("Roboter steuern")
        time.sleep(2)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=kamera_task)
    p2 = multiprocessing.Process(target=roboter_task)
    p1.start()
    p2.start()
