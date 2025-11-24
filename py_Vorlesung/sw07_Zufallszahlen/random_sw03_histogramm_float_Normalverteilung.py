import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm  # optional für PDF-Overlay

# Reproduzierbarkeit (optional)
rng = np.random.default_rng(seed=42)

# 10.000 Zufallszahlen ~ Normalverteilung N(mu, sigma)
mu, sigma = 0.0, 1.0
data = rng.normal(loc=mu, scale=sigma, size=10_000)  # Normalverteilte Samples [web:35]

# Histogramm (als Dichte) und theoretische PDF
plt.figure(figsize=(8, 4))
plt.hist(data, bins=50, density=True, alpha=0.6, edgecolor="black")  # Dichte-Normierung [web:4]

# PDF-Overlay
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 400)
pdf = norm.pdf(x, loc=mu, scale=sigma)
plt.plot(x, pdf, "r", linewidth=2, label="N(μ, σ) PDF")  # theoretische Dichte [web:48]

plt.title("Normalverteilung: Histogramm + PDF (μ=0, σ=1)")
plt.xlabel("Wert")
plt.ylabel("Dichte")
plt.legend()
plt.tight_layout()
plt.show()
