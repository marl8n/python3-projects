
def contador_de_caracteres(cadena_de_texto):
    minusculas = 0
    mayusculas = 0
    numeros = 0
    espacios = 0
    desconocidos = 0

    for letra in cadena_de_texto:
        if letra >= 'a' and letra <= 'z': #en python and, en otros &&
            minusculas += 1
        elif letra >= 'A' and letra <= 'Z':
            mayusculas += 1
        elif letra >= '0' and letra <= '9':
            numeros += 1
        elif letra >= ' ':
            espacios += 1

    return (minusculas, mayusculas, numeros, espacios)


def main():
    while True:
        cadena_de_texto = input('Ingrese una cadena de texto')
        longitud = len(cadena_de_texto)
        min, mayus, num, esp = contador_de_caracteres(cadena_de_texto)
        print(f'Su cadena tiene: {min} minusculas, {mayus} mayusculas, {num} numeros, {esp} espacios y la longitud es de {longitud}.(hubo {desc} caracteres desconocidos)')
        continuar = input('Desea continuar (ingrese si o no)')
        if continuar.lower() == 'si':
            continue
        else:
            break

if __name__ == '__main__':
    main()
