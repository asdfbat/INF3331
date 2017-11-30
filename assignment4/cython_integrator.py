from cython_integrator import cython_integrate, cython_integrate2

if __name__ == "__main__":
    import time
    from numpy_integrator import numpy_integrate
    f = lambda x: x**2
    a = 0; b = 1
    N = int(4e7)

    start_time = time.clock()
    numpy_integrate(f, a, b, N)
    end_time = time.clock()
    python_time = end_time - start_time

    start_time = time.clock()
    cython_integrate(f, a, b, N)
    end_time = time.clock()
    numpy_time = end_time - start_time

    print("Time used by Numpy = %.4fs." % python_time)
    print("Time used by Numba = %.4fs." % numpy_time)
    print("Numpy is a factor %.1f times faster than classic Python." % (python_time/numpy_time) )
