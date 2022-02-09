import math
import numpy as np
from scipy.optimize import minimize_scalar
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
    output = f"{nPr(n-1, n-1)*(c-1)*n} * (1-{char}) * {char}**({n-1})/{(c-1)**(n-1)}"
    
    if n == c: return output
    
    return output + f" + {nPr(c-1, n)} * {char}**({n})/{(c-1)**n}"

def func(n, c):
    a = nPr(n-1, n-1)
    b = (c-1)
    c = (n-1)
    d = (c-1)**(n-1)
    e = nPr(c-1, n)
    
    f = lambda x: (nPr(n-1, n-1)*(c-1)*n*(1-x) * (x/(c-1))**(n-1)) * -1
    res = minimize_scalar(f, bounds=(1, 10), method='bounded')
    return res.x

def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    n_max = y.argmax()
    plt.plot(x[n_max],y[n_max],'o')
    plt.text(1, 1, str(x[n_max]))
    plt.show()
    
def get_max(n, c):
    graph(equation_2(n, c, "x"), np.arange(-20, 20, 0.001))
    
print(equation(2, 2, "x"))
    