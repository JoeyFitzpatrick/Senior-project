from math import floor

def first_n_cubes(n):
    if n == 1: return 1
    return n**3 + first_n_cubes(n - 1)

def XYZ(r, q, n):
    if n == 1: return r
    elif n % 2 == 1: 
        return XYZ(r, q, n - 1) + (n - 1) * q
    else: 
        return XYZ(r, q, n - 1) - (n - 1) * q

def ABC(r, q, n):
    return r + (-1)**(n-1) * floor(n/2) * q

def algo(r, q, n):
    if n % 2 == 0:
        return r - (n/2) * q
    else: 
        return r + ((n-1)/2) * q


def compute(n):
    if n == 0 or n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            temp = b
            b = b + a
            a = temp
        return b

def recursiveFib(n):
    if n == 2 or n == 1:
        return 1
    else:
        return recursiveFib(n - 1) + recursiveFib(n - 2)

print(recursiveFib(5))
print(compute(5))
