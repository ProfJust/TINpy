# turtle_graphics.py
import turtle as t  # Das gesamte Fenster

# - Instanzierung --
kroete = t.Turtle()   # Instanziere ein Objekt der Klasse turtle()
kroete.shape("turtle")
kroete.speed(3)
# t.tracer(False)  # alles sofort zeichnen => False


def seite_zeichnen(seitenlaenge, winkel):
    kroete.forward(seitenlaenge)
    kroete.left(winkel)


def quadrat_zeichnen():
    for ecke in range(4):
        seite_zeichnen(100, 90)


def sechseck_zeichnen():
    for ecke in range(6):
        seite_zeichnen(80, 60)


def spirale_zeichnen():
    s = 5    # Seitenlänge
    w = 90   # Winkel
    for ecke in range(100):
        seite_zeichnen(s, w)
        s = s + 5


def vieleck_zeichnen(seitenlaenge, anzahl_ecken):
    winkel = 360 / anzahl_ecken
    for ecke in range(anzahl_ecken):
        seite_zeichnen(seitenlaenge, winkel)


# ---- Main ----
# quadrat_zeichnen()
# sechseck_zeichnen()
kroete.penup()
kroete.goto(0.0, -200.0)
kroete.pendown()
vieleck_zeichnen(50, 16)
# spirale_zeichnen()
t.done()         # Fenster offen halten