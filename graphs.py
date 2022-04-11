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


def graph_n_given_m(n, m):
    x = [i for i in range(1, n)]
    y = (m-1)/m
    p = [coop_eq(i, m) for i in range(1, n)]
    
    fig, ax = plt.subplots()

    plt.plot(x, y)
    plt.show()
    
    
def graph_m_given_n(n, m):
    x1 = [i for i in range(n+1, m)]
    y1 = [(i-1)/i for i in range(n+1, m)]

    plt.plot(x1, y1, label="20 nodes", linewidth=3)
    plt.ylabel("Simulation result")
    plt.title(f"Proportion of non-conflicting result to 10,000 simulations")
    plt.show()



graph_m_given_n(20, 40)
