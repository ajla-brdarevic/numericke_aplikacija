import numpy as np

# Funkcija parsira string koji predstavlja matematičku funkciju
def parsiraj_funkciju(function_str):
    replaced_str = (function_str.replace('^', '**')  # Zamjenjuje ^ sa ** za potenciju u Pythonu
                    .replace('e^', 'np.exp')  # Ispravna eksponencijalna funkcija, koristi se np.exp
                    .replace('exp', 'np.exp')  # Zamjena exp sa np.exp za eksponencijalnu funkciju
                    .replace('e', 'np.e')  # Zamjenjuje e sa np.e, ispravno korištenje broja e
                    .replace('sin', 'np.sin')  # Sinus funkcija koristi np.sin
                    .replace('cos', 'np.cos')  # Kosinus funkcija koristi np.cos
                    .replace('tan', 'np.tan')  # Tangens funkcija koristi np.tan
                    .replace('asin', 'np.arcsin')  # Arcsin koristi np.arcsin
                    .replace('acos', 'np.arccos')  # Arccos koristi np.arccos
                    .replace('atan', 'np.arctan')  # Arctan koristi np.arctan
                    .replace('sinh', 'np.sinh')  # Sinh funkcija koristi np.sinh
                    .replace('cosh', 'np.cosh')  # Cosh funkcija koristi np.cosh
                    .replace('tanh', 'np.tanh')  # Tanh funkcija koristi np.tanh
                    .replace('pi', 'np.pi')  # Pi se zamjenjuje sa np.pi
                    .replace('ln', 'np.log')  # Logaritamska funkcija prirodni log koristi np.log
                    .replace('log', 'np.log10')  # Logaritamska funkcija koristi np.log10 za logaritamske baze 10
                    .replace('e', 'np.e'))  # Ponovo zamjenjuje e sa np.e
    return replaced_str

# Funkcija koja vraća funkciju koja izračunava vrijednosti za x
def funkcija_iz_stringa(function_str):
    parsiran_str = parsiraj_funkciju(function_str)  # Poziva funkciju parsiraj_funkciju da bi dobila ispravan string
    return lambda x: eval(parsiran_str, {"np": np, "x": x})  # Eval funkcija koristi zamijenjeni string da izračuna vrijednosti

# Trapezna metoda za numeričko izračunavanje integrala
def trapezna_formula(f, a, b, n):
    h = (b - a) / n  # Izračunava veličinu intervala
    suma = 0.5 * (f(a) + f(b))  # Početna suma sa krajnjim tačkama
    for i in range(1, n):  # Petlja koja prolazi kroz sve podintervale
        suma += f(a + i * h)  # Dodaje vrijednosti funkcije na svakom podinterval
    return suma * h  # Vraća ukupnu vrijednost integrala

# Simpsonova metoda za numeričko izračunavanje integrala
def simpsonova_formula(f, a, b, n):
    if n % 2 == 1:  # Provjera da broj podintervala bude paran
        n += 1  # Ako nije paran, povećavamo n za 1
    h = (b - a) / n  # Izračunava veličinu intervala
    suma = f(a) + f(b)  # Početna suma sa krajnjim tačkama
    for i in range(1, n, 2):  # Dodaje 4 puta funkcijske vrijednosti na svim neparnim podintervalima
        suma += 4 * f(a + i * h)
    for i in range(2, n-1, 2):  # Dodaje 2 puta funkcijske vrijednosti na svim parnim podintervalima
        suma += 2 * f(a + i * h)
    return suma * h / 3  # Vraća ukupnu vrijednost integrala podijeljenu sa 3

# Metoda srednje tačke za numeričko izračunavanje integrala
def midpoint_formula(f, a, b, n):
    h = (b - a) / n  # Izračunava veličinu intervala
    suma = 0  # Početna suma
    for i in range(n):  # Petlja koja prolazi kroz sve podintervale
        x = a + (i + 0.5) * h  # Izračunava srednju tačku svakog podintervala
        suma += f(x)  # Dodaje vrijednosti funkcije u sumu
    return suma * h  # Vraća ukupnu vrijednost integrala

# Funkcija koja bira odgovarajuću metodu za integraciju na temelju funkcije
def odaberi_metodu(function_str, a, b, n=1000):
    try:
        f = funkcija_iz_stringa(function_str)  # Pretvara string u funkciju
        test_value = f((a + b) / 2)  # Testira funkciju u sredini intervala
        if np.isnan(test_value):  # Ako funkcija ima neodređene vrijednosti (NaN), vraća grešku
            return None, "Funkcija ima neodređene vrijednosti (NaN)"
        
        if any(op in function_str for op in ['x**', 'x^']):  # Provjera da li funkcija sadrži polinom
            return simpsonova_formula(f, a, b, n), "Koristim Simpsonovu metodu jer je funkcija polinom"
        
        if 'exp' in function_str or 'e**' in function_str or 'np.e' in function_str:  # Provjera da li funkcija sadrži eksponencijalnu funkciju
            return midpoint_formula(f, a, b, n), "Koristim Metodu srednje tačke jer funkcija sadrži eksponencijalne funkcije"
        
        return trapezna_formula(f, a, b, n), "Koristim Trapeznu metodu jer funkcija ne spada u prepoznate kategorije"
    except Exception as e:  # Ako dođe do greške, vraća poruku sa greškom
        return None, f"Greška u odabiru metode: {e}"