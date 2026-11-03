import math

# Pose der Turtle: [x, y, theta]
pose = [0, 0, 0]

# Zielposition
goal = [150, 150]

# Vektor zum Ziel
sx = goal[0] - pose[0]
sy = goal[1] - pose[1]

# Winkel zum Ziel
theta2goal = math.atan2(sy, sx)

print("Winkel zum Ziel:", math.degrees(theta2goal))
print("Vektor:", sx, sy)