
class Koordinaten:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Koordinaten(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Koordinaten(
            self.x - other.x,
            self.y - other.y
        )

    def __str__(self):
        return f"Koordinaten(x={self.x}, y={self.y})"


# Objekte erzeugen
p1 = Koordinaten(10, 20)
p2 = Koordinaten(5, 8)

# Operatoren verwenden
p3 = p1 + p2
p4 = p1 - p2

# Objekte ausgeben
print("Koordinaten 1:", p1)
print("Koordinaten 2:", p2)
print("Addition:", p3)
print("Subtraktion:", p4)
print(p1)
