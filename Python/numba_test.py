import time
from numba import jit, float64, int64, prange

@jit(float64(float64, float64, int64), nopython=True, nogil=True, parallel=True)
def func(x, y, N):
    s = 0
    for i in prange(N):
        s = s + (x+y) + i/400.0
        s = s - 4*x
        print(s)
    return s

start_time = time.clock()
print(func(10, 20, int(4e2)))
end_time = time.clock()
print(end_time-start_time)
