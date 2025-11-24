import random

def monte_carlo_pi(samples=100000):
    inside = 0
    for _ in range(samples):
        # random.random() erzeugt eine Zufallszahl in [0, 1].
        # hier zufällige Punkte (x, y) im Quadrat
        x, y = random.random(), random.random()  
        if x*x + y*y <= 1:  #x² + y² ≤ 1  → Punkt liegt im Kreis (Radius 1)
            inside += 1
    return 4 * inside / samples

print(monte_carlo_pi())

