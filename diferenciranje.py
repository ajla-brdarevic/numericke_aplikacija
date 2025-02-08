import numpy as np

def diferenciraj(function_str):
    def dydx(x, y):
        return eval(function_str.replace('^', '**'))

    x0 = 0  # Početna vrijednost za x
    y0 = 1  # Početna vrijednost za y
    x_end = 10  # Krajnja vrijednost za x
    step_size = 0.1  # Veličina koraka

    x_vals = [x0]
    y_vals = [y0]
    
    x = x0
    y = y0
    
    while x < x_end:
        y = y + step_size * dydx(x, y)
        x = x + step_size
        
        x_vals.append(x)
        y_vals.append(y)
    
    return np.array(x_vals), np.array(y_vals)