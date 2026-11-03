
import turtle
import math


# Pose der Turtle als Klasse
class clPose:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.theta = 0.0


# Ziel als Klasse
class clGoal:

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Vektor als Klasse
class clVector:

    def __init__(self):
        self.x = 0
        self.y = 0

    def getVect(self, g, p):
        self.x = g.x - p.x
        self.y = g.y - p.y


# ---------------------------------------
# Objekte erzeugen
# ---------------------------------------

pose = clPose()
goal = clGoal(150, 150)
s = clVector()

# Vektor zum Ziel berechnen
s.getVect(goal, pose)

# Winkel zum Ziel berechnen
theta2goal = math.atan2(s.y, s.x)

print("Winkel zum Ziel:",
      round(math.degrees(theta2goal), 3))
print("Vektor:", s.x, s.y)


# ---------------------------------------
# Turtle-Grafik
# ---------------------------------------

screen = turtle.Screen()
screen.setup(700, 600)
screen.bgcolor("white")
screen.title("Turtle - Pose und Ziel")

# Turtle erzeugen
robot = turtle.Turtle()
robot.shape("turtle")
robot.color("green")
robot.penup()

# Anfangspose einstellen
robot.goto(pose.x, pose.y)
robot.setheading(pose.theta)

# Ziel markieren
marker = turtle.Turtle()
marker.hideturtle()
marker.penup()
marker.goto(goal.x, goal.y)
marker.dot(15, "red")
marker.write("  Ziel", font=("Arial", 12, "normal"))

# Vektor zum Ziel zeichnen
vector = turtle.Turtle()
vector.hideturtle()
vector.color("blue")
vector.pensize(2)
vector.penup()
vector.goto(pose.x, pose.y)
vector.pendown()
vector.goto(goal.x, goal.y)

# Turtle zum Ziel ausrichten
robot.setheading(math.degrees(theta2goal))

# Turtle zum Ziel fahren lassen
input("go?")
robot.forward(math.hypot(s.x, s.y))

screen.mainloop()
