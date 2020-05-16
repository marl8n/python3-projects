import random

def game(random_number, number_found):
    while not number_found:
        number = int(input('Intenta un número: '))

        if number == random_number:
            print('Felicidades!!! has encontrado el número random')
            number_found = True

        elif number > random_number:
            print('El número random es más pequeño')

        else:
            print('El número random es más grande')


def run():
    number_found = False
    r = int(input('Hasta qué número quieres adivinar'))
    random_number = random.randint(0, r)
    game(random_number, number_found)


if __name__ == '__main__':
    run()
