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
        
        # Provjera za eksponencijalne funkcije (Midpoint formula)
        if 'exp' in function_str or 'e**' in function_str:
            return midpoint_formula(f, a, b, n), "Koristim Metodu srednje tačke jer funkcija sadrži eksponencijalne funkcije"

        # Ako nijedna od specifičnih metoda nije odgovarajuća, koristi Trapeznu metodu
        return trapezna_formula(f, a, b, n), "Koristim Trapeznu metodu jer funkcija ne spada u prepoznate kategorije"
    except Exception as e:
        return None, f"Greška u odabiru metode: {e}"