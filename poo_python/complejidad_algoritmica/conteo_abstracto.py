# Ley de la suma

def f(n):

    for in i range(n):
        print(i)

    for i in range(n):
        print(i)

# O(n) + O(n) = O(n + n) = O(2n) = O(n)

#Ley de suma

def g(n):

    for in i range(n):
        print(i)

    for i in range(n * n):
        print(i)

# O(n) + O(n*n) = O(n + n**2) = O(n**2)

#Ley de multiplicacion

def m(n):

    for i in range(n):
        for j in range(n):
            print(i, j)

# O(n) * O(n) = O(n * n) = O(n**2)

# Recursividad multiple

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci (n = 2)

#O(2**n)
