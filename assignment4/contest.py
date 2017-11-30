from math import sin, pi
from numba_integrator import numba_integrate


def f1(x):
    return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x

def f2(x):
    return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x

def f3(x):
    return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x * 11*sin(x/11)/x

def f4(x):
    return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x

def f5(x):
    return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x * 11*sin(x/11)/x * 13*sin(x/13)/x

def f6(x):
    return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x * 11*sin(x/11)/x * 13*sin(x/13)/x * 15*sin(x/15)/x


a = 1e-20
b = 1e8
N = int(5e10)
for f in [f1, f2, f3, f4, f5, f6]:
    integral_sum = numba_integrate(f, a, b, N)

    with open("report8.txt", "a") as outfile:
        outfile.write( "Computed integral of %s with N=%.1e = %.24f\n" % (f.__name__, N, integral_sum))
