import random
import matplotlib.pyplot as plt # ggf. pip install matplotlib

def monte_carlo_pi_visual(samples=5000):
    inside_x = []
    inside_y = []
    outside_x = []
    outside_y = []

    inside = 0

    for _ in range(samples):
        x = random.random()
        y = random.random()

        # Prüfen ob im Viertelkreis
        if x*x + y*y <= 1:
            inside += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)

    pi_estimate = 4 * inside / samples
    return pi_estimate, inside_x, inside_y, outside_x, outside_y


def main():
    samples = 5000
    pi_estimate, inside_x, inside_y, outside_x, outside_y = monte_carlo_pi_visual(samples)

    plt.figure(figsize=(6, 6))
    plt.scatter(inside_x, inside_y, s=5, label="Inside Circle", alpha=0.6)
    plt.scatter(outside_x, outside_y, s=5, label="Outside Circle", alpha=0.6)

    # Kreislinie zeichnen
    circle = plt.Circle((0, 0), 1, color="black", fill=False, linewidth=2)
    plt.gca().add_patch(circle)

    plt.title(f"Monte Carlo Pi Approximation\nSamples = {samples}, Pi ≈ {pi_estimate:.5f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.legend()
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()


