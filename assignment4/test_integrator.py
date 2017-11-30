from integrator import integrate
from numpy_integrator import numpy_integrate


def test_integral_of_constant_function(tol=1e-10):
    f = lambda x: 2
    a = 0; b = 1
    integral_actual = 2
    print("\nAbsolute error for f(x)=2 (Pure Python)")
    for N in [1, 3, 8, 22, 612, 1403]:
        integral_calculated = integrate(f, a, b, N)
        error = abs(integral_calculated - integral_actual)
        print("(N = %6d) -> %.4e" % (N, error) )
        assert error < tol


def test_integral_of_linear_function(tol=1e-10):
    f = lambda x: 2*x
    a = 0; b = 1
    integral_actual = 1.2
    print("\nAbsolute error for f(x)=2x (Pure Python)")
    for N in [8, 22, 612, 1403, int(1e4), int(1e5)]:
        tol += 1./N    # Need to compensate tolerance for method accuracy.
        integral_calculated = integrate(f, a, b, N)
        error = abs(integral_calculated - integral_actual)
        print("(N = %6d) -> %.4e" % (N, error) )
        assert error < tol


def test_integral_of_constant_function_numpy(tol=1e-10):
    f = lambda x: 2
    a = 0; b = 1
    integral_actual = 2
    print("\nAbsolute error for f(x)=2 (Numpy)")
    for N in [1, 3, 8, 22, 612, 1403]:
        integral_calculated = numpy_integrate(f, a, b, N)
        error = abs(integral_calculated - integral_actual)
        print("(N = %6d) -> %.4e" % (N, error) )
        assert error < tol


def test_integral_of_linear_function_numpy(tol=1e-10):
    f = lambda x: 2*x
    a = 0; b = 1
    integral_actual = 1
    print("\nAbsolute error for f(x)=2x (Numpy)")
    for N in [8, 22, 612, 1403, int(1e4), int(1e5)]:
        tol += 1./N
        integral_calculated = numpy_integrate(f, a, b, N)
        error = abs(integral_calculated - integral_actual)
        print("(N = %6d) -> %.4e" % (N, error) )
        assert error < tol

test_integral_of_constant_function()
test_integral_of_linear_function()
test_integral_of_constant_function_numpy()
test_integral_of_linear_function_numpy()
