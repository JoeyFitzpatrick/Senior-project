import random
import matplotlib.pyplot as plt
import math


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


def nPr(n, r):
    return math.floor(fact(n) / (fact(n - r)))

def coop_eq(n, m):
    p = (m-1)/m
    return (nPr(n, 1)*nPr(m-1, n-1)) * (1-p) * (p/(m-1))**(n-1) + nPr(m-1, n) * (p/(m-1))**n

def arb_eq1(n, m):
    p = 0.75
    return (nPr(n, 1)*nPr(m-1, n-1)) * (1-p) * (p/(m-1))**(n-1) + nPr(m-1, n) * (p/(m-1))**n

def arb_eq2(n, m):
    p = n/m
    return (nPr(n, 1)*nPr(m-1, n-1)) * (1-p) * (p/(m-1))**(n-1) + nPr(m-1, n) * (p/(m-1))**n


def graph_n_given_m(n, m):
    x = [i for i in range(1, n)]
    y = [(m-1)/m for i in range(1, n)]
    p = [coop_eq(i, m) for i in range(1, n)]

    plt.plot(x, y, linewidth=2)
    plt.xlabel("Number of nodes")
    plt.ylabel("Probability of switching")
    plt.title(f"Probability of switching as M = 40, N rises")
    plt.show()
    
    
def graph_m_given_n(n, m):
    x1 = [i for i in range(n, m)]
    y1 = [(i-1)/i for i in range(n, m)]

    plt.plot(x1, y1, linewidth=2)
    plt.xlabel("Number of channels")
    plt.ylabel("Probability of switching")
    plt.title(f"Probability of switching as M rises, N = 10")
    plt.show()
    
def graph_p_given_n(n, m):
    x = [i for i in range(1, n)]
    p = [coop_eq(i, m) for i in range(1, n)]
    p2 = [arb_eq1(i, m) for i in range(1, n)]
    p3 = [arb_eq2(i, m) for i in range(1, n)]

    plt.plot(x, p, linewidth=2, label="Cooperative algorithm")
    plt.plot(x, p2, linewidth=2, label="Constant probability of switching")
    plt.plot(x, p3, linewidth=2, label="Probability of switching = N/M")
    plt.xlabel("Number of nodes")
    plt.ylabel("Probability of non-conflict")
    plt.title(f"Probability of all nodes finding interference-free bands")
    plt.legend(loc="upper right")
    plt.show()



graph_p_given_n(30, 40)

