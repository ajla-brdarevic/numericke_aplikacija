def diferenciraj(function_str):
    def deriviraj_polynomial(term):
        if '^' in term:
            base, exponent = term.split('^')
            new_exponent = int(exponent) - 1
            coefficient = int(base.split('*')[0]) if '*' in base else 1
            new_coefficient = coefficient * int(exponent)
            return f"{new_coefficient}*x^{new_exponent}" if new_exponent != 0 else f"{new_coefficient}"
        elif 'x' in term:
            coefficient = int(term.replace('*x', '').replace(' ', '')) if '*x' in term else 1
            return str(coefficient)
        else:
            return "0"

    terms = function_str.replace(' ', '').replace('-', '+-').split('+')
    derivative_terms = [deriviraj_polynomial(term) for term in terms if term]

    return ' + '.join([term for term in derivative_terms if term != "0"])

# Testiranje funkcije
print(diferenciraj("4*x^3 - 2*x^2 + x"))
