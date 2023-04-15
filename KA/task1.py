from sympy import *
import itertools as it


def all_divs(n):
    pos_divs = divisors(n)
    neg_divs = [-d for d in pos_divs]
    all_divs = neg_divs + pos_divs
    all_divs.sort()
    return all_divs


def is_zz_domain(expr):
    if expr.is_integer:
        return True
    try:
        Poly(simplify(expr), domain='ZZ')
    except CoercionFailed:
        return False
    return True

x = symbols('x')

# F = 16 * x ** 4 + 76 * x ** 3 + 68 * x ** 2 - 76 * x - 84
F = x ** 4 + 2 * x ** 3 - 72 * x ** 2 - 416 * x - 640

X = [i for i in range(degree(F) // 2 + 1)]
Y = [F.subs(x, i) for i in X]

print("X:", X)
print("Y:", Y)

divs = [all_divs(i) for i in Y if i]

combs = list(it.product(*divs))
print(len(combs), combs[:100], "\n")
poly = F
for i in range(len(combs)):
    fY = list(combs[i])
    lag_poly = simplify(interpolating_poly(len(X), x, X, fY))
    divider, reminder = div(poly, lag_poly)
    if reminder == 0 and is_zz_domain(divider):
        print(f"Iteration {i}, combination={combs[i]}, interpolation: {lag_poly}")
        poly = simplify(divider)
    if poly.is_integer:
        break

print("\n", factor(F), "\n")
