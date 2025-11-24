import numpy as np
import matplotlib.pyplot as plt

# Reproduzierbarkeit (optional)
rng = np.random.default_rng(seed=42)

# 100 Zufallszahlen (Integer) im Bereich 0..99
data = rng.integers(low=0, high=100, size=10000)

# Histogramm zeichnen
plt.figure(figsize=(8, 4))
plt.hist(data, bins=100, edgecolor="black")  # 20 Bins für feinere Auflösung
plt.title("Histogramm von 10.000 Zufalls-Integern")
plt.xlabel("Wert")
plt.ylabel("Häufigkeit")
plt.tight_layout()
plt.show()
