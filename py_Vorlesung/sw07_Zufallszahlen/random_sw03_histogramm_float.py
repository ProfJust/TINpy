import numpy as np
import matplotlib.pyplot as plt

# Reproduzierbarkeit (optional)
rng = np.random.default_rng(seed=42)

# 10.000 Zufallszahlen (Float), gleichverteilte Werte im Intervall [0.0, 1.0)
data = rng.random(10_000)  # kontinuierlich gleichverteilt [0, 1) [web:24]

# Histogramm zeichnen
plt.figure(figsize=(8, 4))
plt.hist(data, bins=50, edgecolor="black")  # 50 Bins für feinere Auflösung [web:4]
plt.title("Histogramm von 10.000 Zufalls-Floats (Uniform [0,1))")
plt.xlabel("Wert")
plt.ylabel("Häufigkeit")
plt.tight_layout()
plt.show()
