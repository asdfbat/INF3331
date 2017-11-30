from numpy import sin, pi
from integrator import integrate, midpoint_integrate
from numpy_integrator import numpy_integrate, midpoint_numpy_integrate
from numba_integrator import numba_integrate, numba_integrate_midpoint

def find_N(function, error_tol = 1e-10):
    """
    Calculates the exact N required to reach a certain tolerance.
    "function" parameter must be a callable integrator taking parameters (f, a, b, N)
    """

    integral_actual = 2
    current_N = 2
    former_N = 0
    error = 1
    while error > error_tol:    # First, we go through 2**N to find an N high
        former_N = current_N    # enough to give an error within our tolerance.
        current_N *= 2
        error = abs(integral_actual - function(sin, 0, pi, current_N))

    while abs(current_N - former_N) > 1:    # Then we repeat the bisection method until we find an N that
        error = abs(integral_actual - function(sin, 0, pi, current_N))    # is closest to our exact tolerance.
        if error > error_tol:
            new_N = current_N + abs(current_N - former_N)//2
        else:
            new_N = current_N - abs(current_N - former_N)//2
        former_N = current_N
        current_N = new_N
    return current_N

with open("report6.txt", "w") as outfile:
    outfile.write ( "Steps required to reach error of 1e-10 for integrate = %d\n" % find_N(integrate) )
    outfile.write ( "Steps required to reach error of 1e-10 for midpoint_integrate = %d\n" % find_N(midpoint_integrate) )
    outfile.write ( "Steps required to reach error of 1e-10 for numpy_integrate = %d\n" % find_N(numpy_integrate) )
    outfile.write ( "Steps required to reach error of 1e-10 for midpoint_numpy_integrate = %d\n" % find_N(midpoint_numpy_integrate) )
