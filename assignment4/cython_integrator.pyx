cpdef double cython_integrate(f, double a, double b, int N):
    from numpy import linspace, sum
    cdef double dx = float(b-a)/N
    x_array = linspace(a+dx, b, N)
    f_array = f(x_array)
    integral_sum = sum(f_array)*dx
    return integral_sum

cpdef double cython_integrate2(f, double a, double b, int N):
    cdef double dx
    cdef double integral_sum = 0
    cdef int i
    cdef double x
    dx = (b-a)/N
    for i in range(1, N+1):
        x = a + dx*i
        integral_sum += f(x)*dx
    return integral_sum
