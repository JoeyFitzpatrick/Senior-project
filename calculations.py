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
    output = f"({nPr(n, 1)*nPr(c-1, n-1)}) * (1-{char}) * ({char}^{n-1})/{(c-1)**(n-1)}"
    
    if n == c: return output
    
    return output + f" + {nPr(c-1, n)} * ({char}^{n})/{(c-1)**n}"

def equation_2(n, c, char="p"):
    if n > c: return "n must be <= c"
    output = f"({nPr(n, 1)*nPr(c-1, n-1)}) * (1-{char}) * ({char}**{n-1})/{(c-1)**(n-1)}"
    
    if n == c: return output
    
    return output + f" + {nPr(c-1, n)} * ({char}**{n})/{(c-1)**n}"

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


def get_diff(n, c):
    x = sym.Symbol("x")
    return sym.simplify(sym.diff(eval(equation_2(n, c, "x"))))

def set_diff_equals_zero(n, c):
    x = sym.Symbol("x")
    return sym.solveset(get_diff(n, c), x)

def print_equations(n, c):
    print("raw equation: ", equation(n, c, "x"))
    print("equation to maximize: ", sym.simplify(equation(n, c, "x")))
    print("derivative of function: ", get_diff(n, c))
    print(set_diff_equals_zero(n, c))
    
# final equation: nPr(n, 1) * nPr(c-1, n-1) * (1 * p) * (p/(c-1)^(n-1)) + if c > n, nPr(c-1, n) * (p/(c-1)^n)

#print_equations(2, 3)

c = 1.15
cost = lambda N, M: (N * M)/(M - N)
p_function = lambda N, M: (1/(1+c**cost(N,M)))**(1/(N-1))

cs = 4
ci = 5
def p(m): return (m-1)/m



#print(p_function(40, 50))

# expected cost of switching may equal c^f(N, M)
# f(N, M) = (NM)/(M-N)
# where N = number of nodes, M = number of channels