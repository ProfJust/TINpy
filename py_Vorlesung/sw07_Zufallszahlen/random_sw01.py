import random
# random.seed(42) # bestimmt den Startpunkt in der Zufallszahlenliste
# => reproduzierbar die gleiche Folge von Zufallszahlen

print(random.random())       # 0.374448... 
print(random.randint(1, 6))  # Würfel
print(random.uniform(1, 10)) # Fließkommazahl
print(random.choice(["rot", "grün", "blau"]))

for _ in range(5):
    print(random.gauss(0, 1))

import numpy as np
rng = np.random.default_rng()
rng.integers(0, 10, size=5)  
# -> Array mit 5 Zufallswerten

rng.random(3)
# -> 3 Zufallswerte (float)

rng.normal(0, 1, size=1000)
# -> 1000 Stichproben aus Normalverteilung
