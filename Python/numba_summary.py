from numba import jit, int32, float64

# We add a just-in-time compilation flag in front of a function we wish to compile:
@jit
def func(x, y):
    return x*y

# We can specify input and return types, for more control of the compiler:
@jit( float64(float64, float64) )
def func(x, y):
    return x*y

# To force Numba to use optimized code, and raise an error if it can't, use:
@jit(nopython = True)
