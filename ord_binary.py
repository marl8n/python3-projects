import random


def find_number(lista, number, low, high):
    if low > high:
        return False
    
    mid = int((low + high) / 2)

    if mid == number:
        return True
    elif mid > number:
        return find_number(lista, number, low, mid - 1)
    else:
        return find_number(lista, number, mid + 1, high)


def ordenar(lista, max_i):
    temp = 0
    for i in range(max_i):
        if lista[i] > lista[i + 1]:
            temp = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = temp
        else:
            continue

    return lista


def run():
    lista = list()

    temp = int(input('Intruduzca un valor para generar un rango'))
    for i in range(temp - 1):
        lista.append(random.randint(0, temp))

    lista = ordenar(lista, len(lista) - 1)

    number = int(input('Ingrese un numero para ver si esta en la lista'))
    
    result = find_number(lista, number, 0, len(lista) - 1 )

    if result == True:
        print('El número fue generado en la lista')
        
    else:
        print('El número no está en la lista')
        



if __name__ == '__main__':
    run()
