import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

def f(x):
    return np.sin(x) * (1 + x**2)

def monte_carlo_integrate(x_min, x_max, y_min, y_max, num_points = 10_000, num_experiments = 10):
    areas = []
    
    for _ in range(num_experiments):
        x = np.random.uniform(x_min, x_max, num_points)
        y = np.random.uniform(y_min, y_max, num_points)

        inside_points = np.sum(y <= f(x))

        area = (inside_points / num_points) * (x_max - x_min) * (y_max - y_min)
        areas.append(area)

    return np.mean(areas)

def main():
    a, b = 1, 3
    x = np.linspace(a-1, b+1, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.plot([a, b, b, a, a], [0, 0, max(iy), max(iy), 0], color='blue', linestyle='--')

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(f'Graph of integration f(x) from {a} to {b}')
    plt.grid()
    plt.show()

    monte_result = monte_carlo_integrate(a, b, 0, max(iy), num_points=10000, num_experiments=20)
    print(f"Monte Carlo integral ≈ {monte_result:.6f}")

    result, error = spi.quad(f, a, b)
    print(f"SciPy quad integral = {result:.6f} (±{error:.2e})")

if __name__ == "__main__":
    main()
