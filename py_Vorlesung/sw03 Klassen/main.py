
# Datei: main.py

from roboter import Roboter

# Objekte erzeugen
roboter1 = Roboter("TurtleBot3")
roboter2 = Roboter("Alvik")

# Methoden aufrufen
roboter1.fahren(0.2)
roboter2.fahren(0.1)

roboter1.stoppen()

# Klassenvariable ausgeben
print("Anzahl Roboter:", Roboter.anzahl)

# __str__ verwenden
print(roboter1)
