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


kroete = turtle.Turtle()   # Instanziere ein Objekt der Klasse turtle()
kroete.color('black')
kroete.forward(100)   # Bewegt die Schildkröte 100 Pixel vorwärts
kroete.left(90)       # Dreht die Schildkröte um 90 Grad nach links
kroete.color('red')
kroete.circle(50)     # Zeichnet einen Kreis mit Radius 50 Pixel

# Farbe an bestimmten Pixeln abfragen
kroete.penup()  # Stift anheben, um keine Linien zu zeichnen
kroete.goto(0, 0)  # Gehe zurück zum Ursprung
color_at_origin = get_pixel_color(0, 0)
print(f"Farbe am Ursprung (0,0): {color_at_origin}")
kroete.goto(100, 0)  # Gehe zu (100,0)  x, y
color_at_100_0 = get_pixel_color(100, 10)        
print(f"Farbe bei (100, 10): {color_at_100_0}")

turtle.done()  # Beendet die Turtle-Grafik und hält das Fenster offen
# input("Drücken Sie die Eingabetaste, um das Programm zu beenden...")
