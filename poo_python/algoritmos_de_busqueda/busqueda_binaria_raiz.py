
def busqueda_binaria(numero):
    objetivo = numero
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    return respuesta


def main():
    numero = int(input('Escoge un numero: '))

    print(busqueda_binaria(numero))


if __name__ == '__main__':
    main()
