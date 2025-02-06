from sympy import symbols, integrate, sympify

def integriraj(function_str):
    x = symbols('x')
    func = sympify(function_str)
    integral = integrate(func, x)
    return str(integral)
