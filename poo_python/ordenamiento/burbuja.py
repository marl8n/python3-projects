import random

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n -i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def main():

    tamano_de_lista = int(input('De que tamano sera tu lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = bubble_sort(lista)

    print(lista_ordenada)


if __name__ == '__main__':
    main()
