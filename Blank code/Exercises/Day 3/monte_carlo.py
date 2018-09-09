from math import pi
import random

def monte_carlo(n):
    """ Estimates pi with Monte Carlo Method

    Keyword arguments:
        n (int) -- number of points to use

    Returns:
        Float -- Estimation of pi
    """
    return 0


pi_estimate = monte_carlo(10000)

print("Pi was estimated at {}".format(pi_estimate))
print("The error is {}%".format(100 * abs(pi-pi_estimate)/pi))
