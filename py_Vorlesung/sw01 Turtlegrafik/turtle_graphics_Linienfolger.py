import turtle as t
import math


def get_pixel_color(x, y):
    """Hilfsfunktion: Farbe an Canvas-Position abfragen
    Farbe an bestimmter Canvas-Position (x, y) abfragen
    Ellipse wird als erstes gezeichnet, also ist sie „unter“ der Turtle.
    In get_pixel_color nimmst du dann z.B. nicht das oberste Objekt, sondern explizit das erste Objekt, dessen fill‑Farbe "black" ist:"""
    y_canvas = -y  # y-Achse invertieren (Turtle ↔ Canvas)
    canvas = t.getcanvas()
    ids = canvas.find_overlapping(x, y_canvas, x, y_canvas)
    # if ids:
    #     index = ids[-1]  # oberstes Objekt
    #     color = canvas.itemcget(index, "fill")
    #     if color:
    #         return color

    # von oben nach unten durchgehen und erstes schwarzes Objekt nehmen
    for obj_id in reversed(ids):
        color = canvas.itemcget(obj_id, "fill")
        if color in ("black", "#000000"):
            return "black"
    return "white"


def search_line(frog):
    """Vom Ursprung aus fahren, bis der Sensor schwarz sieht."""
    step = 0.5
    sensor_offset = 3

    while True:
        x = frog.xcor()
        y = frog.ycor()
        heading = frog.heading()

        sensor_x = x + sensor_offset * math.cos(math.radians(heading))
        sensor_y = y + sensor_offset * math.sin(math.radians(heading))

        color = get_pixel_color(sensor_x, sensor_y)
        print(f"Sensor at ({sensor_x:.1f}, {sensor_y:.1f}) sees color: {color}")

        if color == "black":
            # Linie gefunden
            break
        else:
            frog.forward(step)


def follow_line(frog):
    """Einfache Linienfolger-Logik, nachdem die Linie gefunden wurde.
    Statt eines Sensors direkt vorne nimm zwei leicht versetzte Sensoren 
    links/rechts. 
    So kannst du „zu weit links“ vs. „zu weit rechts“ unterscheiden 
    und musst nicht ständig hin‑ und herdrehen."""
    step = 1  # Schrittweite
    turn_soft = 2  # sanftes Drehen, wenn Linie leicht versetzt ist
    turn_hard = 6  # stärkeres Drehen, wenn Linie verloren oder stark gekrümmt
    sensor_offset_forward = 10  # Sensor vor der Mitte
    sensor_offset_side = 6  # seitlicher Versatz für linke/rechte Sensoren

    while True:
        x = frog.xcor()  # aktuelle Position
        y = frog.ycor()
        heading = frog.heading()  # aktuelle Richtung in Grad
        h_rad = math.radians(heading)  # Richtung in Bogenmaß für trigonometrische Funktionen

        # Sensorposition 1 vor der Mitte
        front_x = x + sensor_offset_forward * math.cos(h_rad)  
        front_y = y + sensor_offset_forward * math.sin(h_rad)

        # Sensorposition 2 etwas links vorne
        left_x = front_x - sensor_offset_side * math.sin(h_rad)
        left_y = front_y + sensor_offset_side * math.cos(h_rad)

        # Sensorposition 3 etwas rechts vorne
        right_x = front_x + sensor_offset_side * math.sin(h_rad)
        right_y = front_y - sensor_offset_side * math.cos(h_rad)

        # Sensorfarben abfragen
        c_front = get_pixel_color(front_x, front_y)
        c_left  = get_pixel_color(left_x, left_y)
        c_right = get_pixel_color(right_x, right_y)

        # Entscheidungslogik
        if c_front == "black":
            # gut im Zentrum
            frog.forward(step)
        elif c_left == "black" and c_right != "black":
            # Linie eher links: sanft links
            frog.left(turn_soft)
            frog.forward(step)
        elif c_right == "black" and c_left != "black":
            # Linie eher rechts: sanft rechts
            frog.right(turn_soft)
            frog.forward(step)
        elif c_left == "black" and c_right == "black":
            # stark gekrümmt / dicke Linie: härter drehen
            frog.left(turn_hard)  # oder abhängig von letzter Richtung
            frog.forward(step)
        else:
            # Linie verloren: leichte Suchbewegung
            frog.left(turn_soft)


def setup_screen():
    screen = t.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Turtle-Linienfolger (Ellipse)")
    return screen   


def draw_ellipse():
    drawer = t.Turtle()
    drawer.hideturtle()
    drawer.speed(0)
    drawer.color("black")
    drawer.pensize(5)
    a = 250  # Halbachse x
    b = 150  # Halbachse y
    drawer.penup()
    drawer.goto(a, 0)
    drawer.pendown()

    for angle in range(361):
        theta = math.radians(angle)
        x = a * math.cos(theta)
        y = b * math.sin(theta)
        drawer.goto(x, y)


def setup_frog():
    frog = t.Turtle()
    frog.shape("turtle")
    frog.color("green")
    frog.speed(1)  # 0 = maximale Geschwindigkeit, 1 = langsamste Geschwindigkeit
    frog.penup()
    # Startposition: Ursprung, nach rechts schauend
    frog.goto(0, 0)
    frog.setheading(20)    # 0° = nach rechts
    return frog


def main():
    setup_screen()
    draw_ellipse()
    frog = setup_frog()
    
    # -------------------------------------------------
    # Zuerst Linie suchen, dann folgen
    # -------------------------------------------------
    search_line(frog)   # vom Ursprung aus losfahren, bis Linie erreicht
    follow_line(frog)   # dann der Linie folgen
    t.done()


if __name__ == "__main__":
    main()

