# @profile
def func(x, N):
    s = 0
    for i in range(N):
        s += i*x + func2(i)
    return s

# @profile
def func2(i):
    x = 2*i+1
    return x

print(func(10, 100000))
