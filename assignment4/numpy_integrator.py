def numpy_integrate(f, a, b, N):
    from numpy import linspace, sum, shape, full
    dx = float(b-a)/N
    x_array = linspace(a+dx, b, N)
    f_array = f(x_array)
    if shape(f_array) == ():  # In case f returns a number and not an array.
        f_array = full(N, f_array)
    integral_sum = sum(f_array)*dx
    return integral_sum

def midpoint_numpy_integrate(f, a, b, N):
    from numpy import linspace, sum, shape, full
    dx = float(b-a)/N
    x_array = linspace(a+dx/2, b-dx/2, N)
    f_array = f(x_array)
    if shape(f_array) == ():  # In case f returns a number and not an array.
        f_array = full(N, f_array)
    integral_sum = sum(f_array)*dx
    return integral_sum


if __name__ == "__main__":  # Speed comparison with pure Python.
    import time
    from integrator import integrate
    f = lambda x: x**2
    a = 0; b = 1
    N = int(4e7)

    start_time = time.clock()
    integrate(f, a, b, N)
    end_time = time.clock()
    python_time = end_time - start_time

    start_time = time.clock()
    numpy_integrate(f, a, b, N)
    end_time = time.clock()
    numpy_time = end_time - start_time

    with open("report3.txt", "w") as outfile:
        outfile.write("Time used by classic Python = %.4fs.\n" % python_time)
        outfile.write("Time used by Numpy = %.4fs.\n" % numpy_time)
        outfile.write("Numpy is a factor %.1f times faster than pure Python." % (python_time/numpy_time) )
