# turtle_graphics.py
import turtle


def get_pixel_color(x, y):
    """ Farbe an bestimmtem Pixel (x, y) abfragen  """
    y = -y  # Koordinatensystem anpassen
    canvas = turtle.getcanvas()
    ids = canvas.find_overlapping(x, y, x, y)
    if ids:
        index = ids[-1]
        color = canvas.itemcget(index, "fill")
        if color:
            return color
    return "white"


turtle = turtle.Turtle()   # Instanziere ein Objekt der Klasse turtle()
turtle.forward(100)   # Bewegt die Schildkröte 100 Pixel vorwärts
turtle.left(90)       # Dreht die Schildkröte um 90 Grad nach links
turtle.color('red')
turtle.circle(50)     # Zeichnet einen Kreis mit Radius 50 Pixel

# Farbe an bestimmten Pixeln abfragen
turtle.goto(0, 0)  # Gehe zurück zum Ursprung
color_at_origin = get_pixel_color(0, 0)
print(f"Farbe am Ursprung (0,0): {color_at_origin}")
turtle.goto(100, 0)  # Gehe zu (100,0)
color_at_100_0 = get_pixel_color(100, 0)        
print(f"Farbe bei (100,0): {color_at_100_0}")

turtle.done()         # Fenster offen halten
input("Drücken Sie die Eingabetaste, um das Programm zu beenden...")
