

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo( n - 1 ) + fibonacci_recursivo ( n - 2 )


def fibonacci_optimizado(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_optimizado( n - 1, memo ) + fibonacci_optimizado( n - 2, memo )
        memo[n] = resultado

        return resultado


if __name__ == '__main__':
    n = int(input('Escoge un numero: '))
    print(fibonacci_optimizado(n))
#    print(fibonacci_recursivo(n))
