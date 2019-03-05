from math import pi
import random

def monte_carlo(n):
    """ Estimates pi with Monte Carlo Method

    Keyword arguments:
        n (int) -- number of points to use

    Returns:
        Float -- Estimation of pi
    """
    in_circle = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            in_circle += 1

    return 4 * in_circle / n


pi_estimate = monte_carlo(10000)

print("Pi was estimated at {}".format(pi_estimate))
print("The error is {}%".format(100 * abs(pi-pi_estimate)/pi))