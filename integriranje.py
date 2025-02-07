import numpy as np

# Trapezna formula
def trapezna_formula(f, a, b, n):
    h = (b - a) / n
    suma = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        suma += f(a + i * h)
    return suma * h

# Simpsonova formula
def simpsonova_formula(f, a, b, n):
    if n % 2 == 1:
        n += 1  # Broj podintervala mora biti paran
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        suma += 2 * f(a + i * h)
    return suma * h / 3

# Midpoint formula
def midpoint_formula(f, a, b, n):
    h = (b - a) / n
    suma = 0
    for i in range(n):
        x = a + (i + 0.5) * h
        suma += f(x)
    return suma * h

# Rombergov algoritam
def romberg(f, a, b, max_iter=10):
    R = np.zeros((max_iter, max_iter))
    R[0, 0] = trapezna_formula(f, a, b, 1)
    for i in range(1, max_iter):
        R[i, 0] = trapezna_formula(f, a, b, 2**i)
        for k in range(1, i+1):
            R[i, k] = (4**k * R[i, k-1] - R[i-1, k-1]) / (4**k - 1)
    return R[max_iter-1, max_iter-1]

# Gauss-Legendreova integracija
def gauss_legendre(f, a, b, n):
    # Gauss-Legendre weight and nodes for n=2
    if n == 2:
        x = [-1/np.sqrt(3), 1/np.sqrt(3)]
        w = [1, 1]
    else:
        raise NotImplementedError("For n != 2, implementation needs adjustment.")
    
    # Mapping nodes to [a, b]
    mid = (b + a) / 2
    h = (b - a) / 2
    integral = 0
    for i in range(len(x)):
        integral += w[i] * f(mid + h * x[i])
    return integral * h

def odaberi_metodu(f, a, b, n=1000):
    try:
        test_value = f((a + b) / 2)
        if np.isnan(test_value):
            return None, "Funkcija ima neodređene vrijednosti (NaN)"
        
        # Konvertiramo funkciju u string radi lakše provjere tipa funkcije
        function_str = str(f)

        # Provjera za polinome (Simpsonova metoda)
        if 'x**' in function_str or 'x^' in function_str:
            return simpsonova_formula(f, a, b, n), "Koristim Simpsonovu metodu jer je funkcija polinom"
        
        # Provjera za trigonometrijske funkcije (Gauss-Legendreova metoda)
        if 'sin' in function_str or 'cos' in function_str or 'tan' in function_str:
            return gauss_legendre(f, a, b, 2), "Koristim Gauss-Legendreovu metodu jer funkcija sadrži trigonometrijske funkcije"
        
        # Provjera za eksponencijalne funkcije (Midpoint formula)
        if 'exp' in function_str or 'e**' in function_str:
            return midpoint_formula(f, a, b, n), "Koristim Metodu srednje tačke jer funkcija sadrži eksponencijalne funkcije"
        
        # Provjera za logaritamske funkcije (Rombergov algoritam)
        if 'log' in function_str or 'ln' in function_str:
            return romberg(f, a, b), "Koristim Rombergov algoritam jer funkcija sadrži logaritamske funkcije"

        # Ako nijedna od specifičnih metoda nije odgovarajuća, koristi Trapeznu metodu
        return trapezna_formula(f, a, b, n), "Koristim Trapeznu metodu jer funkcija ne spada u prepoznate kategorije"
    except Exception as e:
        return None, f"Greška u odabiru metode: {e}"
