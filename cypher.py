# abj)|":><'/,12"CDFLMPRVX


KEYS = {
        'a': '.',
        'b': '@',
        'c': 'w',
        'd': 'K',
        'e': '#',
        'f': '$',
        'g': 'o',
        'h': 'p',
        'i': 'H',
        'j': 'U',
        'k': 'z',
        'l': '!',
        'm': 'm',
        'n': 'h',
        'o': 'v',
        'p': '7',
        'q': 'B',
        'r': '(',
        's': 't',
        't': 's',
        'u': 'c',
        'v': '4',
        'w': 'J',
        'x': 'Z',
        'y': '`',
        'z': '~',
        'A': '1',
        'B': '4',
        'C': 'y',
        'D': 'i',
        'E': '=',
        'F': 'I',
        'G': 'x',
        'H': '^',
        'I': 'A',
        'J': '+',
        'K': 'G',
        'L': '?',
        'M': 'g',
        'N': ';',
        'O': '{',
        'P': 'k',
        'Q': 'S',
        'R': ']',
        'S': '5',
        'T': '9',
        'U': 'O',
        'V': '&',
        'W': '3',
        'X': '8',
        'Y': 'n',
        'Z': 'r',
        '1': 'T',
        '2': 'f',
        '3': 'W',
        '4': 'u',
        '5': 'Y',
        '6': '-',
        '7': '}',
        '8': 'Q',
        '9': '_',
        '0': '6',
        '?': '[',
        ',': 'E',
        '.': 'D',
        '!': 'e',
        }

def cypher(message):
    words = message.split(' ')
    cypher_message = list()

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    return ' '.join(cypher_message)

def decypher(message):
    words = message.split(' ')
    decipher_message = list()
    
    for word in words:
        decipher_word = ''

        for letter in word:

            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)

    return ' '.join(decipher_message)

def run():

    while True:

        command = input('''
                    
                    Bienvenido a criptografía. ¿Qué deseas hacer?

                    [c]ifrar mensaje
                    [d]escifrar
                    [s]alir

                ''')
        if command == 'c':
            message = input('cifrar')
            cypherMessage = cypher(message)
            print(cypherMessage)
        elif command == 'd':
            message = input('Escribe tu mensaje cifrado')
            decypher_message  = decypher(message)
            print(decypher_message)
        elif command == 's':
            print('')
            break
        else:
            print('Comando no encontrado')



if __name__ == '__main__':
    run()
