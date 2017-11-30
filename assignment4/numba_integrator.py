from numba import jit, njit, prange

def numba_integrate(f, a, b, N):  # Making a wrapper-function was the only way I could find of taking a
    g = njit(f)                   # function as argument (without requiring it to already be a jit-compiled).
    @jit(nopython=True, parallel=True)
    def integrate(a, b, N):
        dx = (b-a)/N
        integral_sum = 0
        for i in prange(1, N+1):
            x = a + dx*i
            integral_sum += g(x)
        return integral_sum*dx
    return integrate(a, b, N)

def numba_integrate_midpoint(f, a, b, N):
    g = njit(f)
    @jit(nopython=True, parallel=True)
    def integrate(a, b, N):
        dx = (b-a)/N
        integral_sum = 0
        for i in prange(1, N+1):
            x = a + dx*(i - 0.5)
            integral_sum += g(x)
        return integral_sum*dx
    return integrate(a, b, N)

"""
Numba has two main advantages compared to Numpy.
The speed is superior, if the arithmetic is
properly implemented. It even supports native parallelization.
Secondly, Numpy scales memory linearly with N, due to the need of storing arrays.
Numba doesn't scale memory with N at all. Due to this being a memory-heavy task,
Numpy uses up a usual computer's memory for runtimes as low as 5-20 seconds.
"""


if __name__ == "__main__":  # Speed comparison with Numpy
    import time
    from numpy_integrator import numpy_integrate
    import multiprocessing  # In order to access the nr of CPU-cores.
    nr_cpus = multiprocessing.cpu_count()
    a = 0; b = 1
    f = lambda x: x**2
    N = int(4e8)  # Sadly, we can't push the test further than this due to Numpy's memory usage.

    start_time = time.clock()
    numpy_integrate(f, a, b, N)
    end_time = time.clock()
    numpy_time = end_time - start_time

    start_time = time.clock()
    numba_integrate(f, a, b, N)
    end_time = time.clock()
    numba_time = (end_time - start_time) / nr_cpus  # time.clock() shows total CPU-time.
                                                # Since Numba is parallelized, we devide by
                                                # number of cores to find actual time.

    with open("report4.txt", "w") as outfile:
        outfile.write("Time used by Numpy = %.4fs.\n" % numpy_time)
        outfile.write("Time used by Numba = %.4fs.\n" % numba_time)
        outfile.write("Numba is a factor %.1f times faster than Numpy." % (numpy_time/numba_time) )
