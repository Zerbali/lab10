# "An algorithm must be developed to approximately find the root of the following equation within a given interval using the Newton's method."


def f(x):
    return x - 2 * (x ** 0.25) 

def f_prime(x):
    return 1 - 2 * (0.25 * x ** (-0.75)) 

def newton_method(x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        fx = f(x0)
        fpx = f_prime(x0)
        if fpx == 0:
            print("Zero derivative. No solution found.")
            return None
        x1 = x0 - fx / fpx
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

x0 = 3.5

root = newton_method(x0)
print(f"Approximate root using Newton's method: {root:.6f}")
