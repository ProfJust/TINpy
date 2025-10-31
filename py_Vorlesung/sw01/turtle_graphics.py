# turtle_graphics.py
import turtle

t = turtle.Turtle()   # Instanziere ein Objekt der Klasse turtle()
t.forward(100)   # Bewegt die Schildkröte 100 Pixel vorwärts
t.left(90)       # Dreht die Schildkröte um 90 Grad nach links
t.color('red')
t.circle(50)     # Zeichnet einen Kreis mit Radius 50 Pixel

#t.done()         # Fenster offen halten
input()