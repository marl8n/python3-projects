import random


def busqueda_binaria(lista, comienzo, final, objetivo):

    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if objetivo == medio:
        return True
    elif objetivo < lista[medio]:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)
    elif objetivo > lista[medio]:
        return busqueda_binaria(lista, medio + 1, final, objetivo)


def main():
    tamano_de_lista = int(input('De que tamano quieres la lista: '))
    objetivo = int(input('Que numero quieres encontrar: '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')


if __name__ == '__main__':
    main()
