import math
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


def fact(n):
    if n <= 1: return 1
    return n * fact(n-1)

def nPr(n, r):
    return math.floor(fact(n) / (fact(n - r)))

def equation(n, c, char="p"):
    if n > c: return "n must be <= c"
    output = f"{nPr(n-1, n-1)*(c-1)*n} * (1-{char}) * {char}^{n-1}/{(c-1)**(n-1)}"
    
    if n == c: return output
    
    return output + f" + {nPr(c-1, n)} * {char}^{n}/{(c-1)**n}"

def equation_2(n, c, char="p"):
    if n > c: return "n must be <= c"
    output = f"{nPr(n-1, n-1)*(c-1)*n} * (1-{char}) * {char}**{n-1}/{(c-1)**(n-1)}"
    
    if n == c: return output
    
    return output + f" + {nPr(c-1, n)} * {char}**{n}/{(c-1)**n}"

def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    n_max = y.argmax()
    plt.plot(x[n_max],y[n_max],'o')
    plt.text(1, 1, str(x[n_max]))
    plt.show()
    
def get_max_graph(n, c):
    graph(equation_2(n, c, "x"), np.arange(0, 20, 0.01))

def get_max_test(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    n_max = y.argmax()
    return x[n_max]

def get_max(n, c):
    return get_max_test(equation_2(n, c, "x"), np.arange(0, 20, 0.01))


#

def get_diff(n, c):
    x = sym.Symbol("x")
    return sym.diff(eval(equation_2(n, c, "x")))

def set_diff_equals_zero(n, c):
    x = sym.Symbol("x")
    return sym.solveset(get_diff(n, c), x)

print("equation to maximize: ", equation(2, 5, "x"))
print("derivative of function: ", get_diff(2, 5))
print(set_diff_equals_zero(2, 5))
