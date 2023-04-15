from sympy import *
import itertools as it

x = symbols('x')
y = symbols('y')
z = symbols('z')


def printG(G):
    print(f"G: {len(G)=}")
    print(*G, sep=",\n", end="\n\n")


funcs = [
    x ** 2 + z ** 2 * y + y * z,
    y ** 2 - z * x + x,
    x * y + z ** 2 - 1
]


def spoly(p, q):
    return simplify(lcm(LT(p), LT(q)) * (p / LT(p) - q / LT(q)))


def lt(x):
    if total_degree(x) == 0:
        return x
    return LT(x)


def remainder(f, G):
    h = f
    r = 0
    qs = [0 for i in G]
    while h != 0:
        for i in range(len(G)):
            h = simplify(h)
            divres = div(lt(h), lt(G[i]), domain=ZZ)
            if divres[0] != 0:
                qs[i] += divres[0]
                h -= divres[0] * G[i]
                break
        else:
            r += lt(h)
            h -= lt(h)
    return r, qs


def groebner_basis(F):
    G = F
    C = [(G[i], G[j]) for i in range(len(G)) for j in range(i + 1, len(G))]
    i = 1
    while C:
        (f, g), *C = C
        print(f"Step {i} (left combinations {len(C)}):")
        i += 1
        # print(f"G: {G}")
        printG(G)
        print(f"f: {f}\ng: {g}")
        sp = spoly(f, g)
        print(f"spoly(f, g): {sp}")
        h = remainder(sp, G)[0]
        info = "add it to G" if h != 0 else 'ignore'
        print(f"remainder(spoly, G): {h} ({info})")
        if h != 0:
            C += [(i, h) for i in G]
            G += [h]
        print()
    return G


G = groebner_basis(funcs)

printG(G)


def reduce_basis(G):
    for i in range(len(G)):
        G[i] /= LC(G[i])

    for i, j in it.product(G, G):
        if i == j:
            continue
        if div(LT(i), LT(j))[1] == 0:
            G.remove(i)


reduce_basis(G)

print("Reduced ", end="")
printG(G)

print(groebner(funcs, (x, y, z)))
