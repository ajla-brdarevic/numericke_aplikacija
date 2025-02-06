from sympy import symbols, diff, sympify

def diferenciraj(function_str):
    x = symbols('x')
    func = sympify(function_str)
    derivative = diff(func, x)
    return str(derivative)
