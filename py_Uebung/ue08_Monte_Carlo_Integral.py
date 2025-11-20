import random

def monte_carlo_integral_x2(samples=100000):
    a = 0.0   # untere Grenze
    b = 3.0   # obere Grenze

    s = 0.0   # Summe der Funktionswerte

    for _ in range(samples):
        x = random.uniform(a, b)  # Zufallszahl in [0, 3]
        fx = x**2                 # f(x) = x^2
        s += fx

    mean_f = s / samples          # Mittelwert von f(x)
    integral_estimate = (b - a) * mean_f  # (b-a) * Mittelwert

    return integral_estimate

approx = monte_carlo_integral_x2()
print("Monte-Carlo-Approximation:", approx)
print("Exakter Wert: 9.0")
