

def run():
    word = input('Ingrese una palabra para verificar si es palíndromo')
    if word == word[::-1]:
        print('La palabra {} es palíndromo'.format(word))
        
    else:
        print('La palabra {} no es palíndromo'.format(word))


if __name__ == '__main__':
    run()
