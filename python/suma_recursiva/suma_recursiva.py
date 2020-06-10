

def sumaRecursiva(times, number):
    if times <= 0:
        print('Su resultado es')
        return number

    number += int(input('annade el numero que quieres sumar: '))
    times -= 1
    return sumaRecursiva(times, number)


def run():
    times = int(input('Cuantas veces quieres sumar? '))
    number = 0
    print(sumaRecursiva(times, number))


if __name__ == '__main__':
    run()
