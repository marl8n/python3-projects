def character_repeat(lword):
    t_lword = lword
    print(t_lword)
    temp = 0
    for i in range(len(t_lword)):
        temp = 0
        for j in range(len(t_lword)):
            if t_lword[i] == t_lword[j]:
                temp += 1
            else:
                continue

        if temp == 1:
            return t_lword[i]
        else:
            continue
    return 'Todos los valores se repiten'
        

def run():
    lword = (input('Introduzca una secuencia de caracteres'))
    result = character_repeat(lword)
    print(result)

if __name__ == '__main__':
    run()
