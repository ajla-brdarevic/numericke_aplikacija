import numpy as np

def diferenciraj(function_str):
    def dydx(x, y):
        # Zamjena operatora i funkcija za ispravno izvođenje
        replaced_str = (function_str.replace('^', '**')
                        .replace('e^', 'np.exp')  # Ispravna eksponencijalna funkcija
                        .replace('exp', 'np.exp')
                        .replace('e', 'np.e')  # Broj e ispravno zamijenjen sa np.e                       
                        .replace('sin', 'np.sin')  # Zamjena sin funkcije
                        .replace('cos', 'np.cos')  # Zamjena cos funkcije
                        .replace('tan', 'np.tan')  # Zamjena tan funkcije
                        .replace('asin', 'np.arcsin')  # Zamjena asin funkcije
                        .replace('acos', 'np.arccos')  # Zamjena acos funkcije
                        .replace('atan', 'np.arctan')  # Zamjena atan funkcije
                        .replace('sinh', 'np.sinh')  # Zamjena sinh funkcije
                        .replace('cosh', 'np.cosh')  # Zamjena cosh funkcije
                        .replace('tanh', 'np.tanh')  # Zamjena tanh funkcije
                        .replace('pi', 'np.pi')  # Zamjena pi sa numpy pi
                        .replace('ln', 'np.log')  # Zamjena ln sa numpy logaritmom
                        .replace('log', 'np.log10'))  # Zamjena log sa logaritmom u bazi 10
        return eval(replaced_str)  # Izvršava zamijenjenu funkciju

    # Postavljamo početne vrijednosti za x i y
    x0 = 0  # Početna vrijednost za x
    y0 = 1  # Početna vrijednost za y
    x_end = 10  # Krajnja vrijednost za x
    step_size = 0.1  # Veličina koraka (intervala između tačaka)

    # Kreiramo liste za x i y vrijednosti koje ćemo kasnije vratiti
    x_vals = [x0]
    y_vals = [y0]
    
    # Inicijalizacija početne tačke
    x = x0
    y = y0
    
    # Računanje diferencijacije pomoću Eulerove metode
    while x < x_end:
        # Računanje novog y koristeći trenutnu vrijednost x i y
        y = y + step_size * dydx(x, y)
        # Uvećanje x za veličinu koraka
        x = x + step_size
        
        # Dodavanje novih vrijednosti u liste
        x_vals.append(x)
        y_vals.append(y)
    
    # Vraćamo nizove x i y tačaka kao numpy array
    return np.array(x_vals), np.array(y_vals)