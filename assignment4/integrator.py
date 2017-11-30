def integrate(f, a, b, N):
    dx = float(b-a)/N
    integral_sum = 0
    for i in range(1, N+1):
        x = a + dx*i
        integral_sum += f(x)*dx
    return integral_sum

def midpoint_integrate(f, a, b, N):
    dx = float(b-a)/N
    integral_sum = 0
    for i in range(1, N+1):
        x = a + dx*(i-0.5)
        integral_sum += f(x)*dx
    return integral_sum


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    a = 0; b = 1
    f = lambda x: x**2
    nr_of_Ns = 100
    integral_actual = [1./3]*nr_of_Ns
    integral_calculated = []
    error = []
    for N in range(1, nr_of_Ns):
        integral_calculated.append( integrate(f, a, b, N) )
        error.append( abs(integral_calculated[-1] - integral_actual[0]) )

    plt.plot(error)
    plt.title("Error of N-point numerical integral of $x^2$")
    plt.xlabel("N")
    plt.ylabel("Absolute Error")
    plt.savefig("quadratic_error.pdf")
