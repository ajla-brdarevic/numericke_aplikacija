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

# Metoda za izbor najbolje metode na osnovu vrste funkcije
def odaberi_metodu(f, a, b, n=1000):  # Dodan parametar za broj podintervala
    try:
        test_value = f((a + b) / 2)
        if np.isnan(test_value):  # Ako je funkcija NaN (neodređena vrijednost)
            return None
        
        # Provjera vrste funkcije: ako je polinom, koristit ćemo Simpsonovu metodu
        if np.allclose(f(a), f(b)):  # Ako su vrijednosti funkcije na krajevima intervala iste
            return simpsonova_formula(f, a, b, n)  # Koristi Simpsonovu metodu
        else:
            return trapezna_formula(f, a, b, n)  # Ako nije polinom, koristi trapeznu metodu
    except Exception as e:
        print(f"Greška u odabiru metode: {e}")
        return None
    
