import random
import matplotlib.pyplot as plt
import math
from bisection import bisection


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


def nPr(n, r):
    # Number of ways r different objects can be selected and arranged out of n objects
    return math.floor(fact(n) / (fact(n - r)))


def coop_eq(n, m):
    p = (m-1)/m
    # Formula for calculating probability of all nodes finding interference-free channels
    return (nPr(n, 1)*nPr(m-1, n-1)) * (1-p) * (p/(m-1))**(n-1) + nPr(m-1, n) * (p/(m-1))**n


def cost_func(n, m):
    return (n*m) / (m-n)


# def comp_eq(n, m):
#     return math.pow(1 / (1 + math.pow(1.2, cost_func(n, m))), 1 / (n - 1))

def comp_eq(n, m, cs, ci):
    def inner_eq(p):
        return (1 + p/(1-m))**(n-1) - p**(n-1) - (cs/ci)
    return bisection(inner_eq, 0, 1, 0.001)


def comp_eq_p(n, m, cs, ci):
    p = comp_eq(n, m, cs, ci)
    return (nPr(n, 1)*nPr(m-1, n-1)) * (1-p) * (p/(m-1))**(n-1)


def arb_eq1(n, m, p):
    # p = 0.9
    return (nPr(n, 1)*nPr(m-1, n-1)) * (1-p) * (p/(m-1))**(n-1) + nPr(m-1, n) * (p/(m-1))**n


def arb_eq2(n, m):
    p = n/m
    return (nPr(n, 1)*nPr(m-1, n-1)) * (1-p) * (p/(m-1))**(n-1) + nPr(m-1, n) * (p/(m-1))**n


def arb_eq3(n, m):
    p = 0.7
    return (nPr(n, 1)*nPr(m-1, n-1)) * (1-p) * (p/(m-1))**(n-1) + nPr(m-1, n) * (p/(m-1))**n


def graph_n_given_m(lower_range, upper_range, m):
    # Lower range and upper range define the range of n, the number of nodes
    x = [i for i in range(lower_range, upper_range)]
    y = [coop_eq(i, m) for i in range(lower_range, upper_range)]

    plt.plot(x, y, linewidth=2)
    plt.xlabel("Number of nodes")
    plt.ylabel("Probability of switching")
    plt.title(f"Probability of switching as M = {m}, N rises")
    plt.show()


def graph_m_given_n(n, m):
    x1 = [i for i in range(n, m)]
    y1 = [comp_eq(n, i+1) for i in range(n, m)]

    plt.plot(x1, y1, linewidth=2)
    plt.xlabel("Number of channels")
    plt.ylabel("Probability of switching")
    plt.title(f"Probability of switching as M rises, N = 10")
    plt.show()


def graph_p_given_n(n, m):
    x = [i for i in range(10, n)]
    p = [(comp_eq_p(i, m, 0.2, 0.5)) for i in range(10, n)]
    p2 = [(comp_eq_p(i, m, 0.2, 0.5)) * 0.8 for i in range(10, n)]
    p3 = [arb_eq3(i, m) for i in range(10, n)]

    plt.plot(x, p, linewidth=2, label="Competitive algorithm")
    plt.plot(x, p2, linewidth=2, label="Competitive algorithm with changed strategy")
    plt.plot(x, p3, linewidth=2, label="Arbitrary probability of switching")
    # plt.plot(x, p3, linewidth=2, label="Probability of switching = N/M")
    plt.xlabel("Number of nodes")
    plt.ylabel("Probability of non-conflict")
    plt.title(f"Probability of all nodes finding interference-free bands, M = 30")
    plt.legend(loc="upper right")
    plt.show()


graph_p_given_n(20, 30)
