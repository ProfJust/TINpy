import random
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_integral_x2(samples=2000):
    a = 0.0   # untere Grenze
    b = 3.0   # obere Grenze

    xs = []
    ys = []
    s = 0.0   # Summe der Funktionswerte

    for _ in range(samples):
        x = random.uniform(a, b)  # Zufallszahl in [0, 3]
        fx = x**2                 # f(x) = x^2
        xs.append(x)
        ys.append(fx)
        s += fx

    mean_f = s / samples                     # Mittelwert der Funktion
    integral_estimate = (b - a) * mean_f     # Monte-Carlo-Formel

    return integral_estimate, xs, ys


# -----------------------------
# Visualisierung
# -----------------------------
def visualize():
    samples = 2000
    estimate, xs, ys = monte_carlo_integral_x2(samples)

    # Plot erstellen
    plt.figure(figsize=(8, 6))

    # Zufallspunkte
    plt.scatter(xs, ys, s=10, alpha=0.3, label="Zufallspunkte")

    # Exakte Funktion
    x_curve = np.linspace(0, 3, 300)
    y_curve = x_curve**2
    plt.plot(x_curve, y_curve, lw=2, label="f(x) = x² (exakt)")

    plt.title(f"Monte-Carlo-Approximation: ∫₀³ x² dx ≈ {estimate:.4f}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    visualize()

    # Ausgabe in der Konsole
    approx, _, _ = m
