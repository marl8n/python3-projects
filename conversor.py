
def main():
    print('Este programa convierte tu moneda')
    money = float(input('Ingresa una cantidad en dolares'))
    change = q_ss(money)
    print('${} Dólares equivalen a ${} quetzales'.format(money, change))

def q_ss(money):
    quetzales = 7.69

    return money * quetzales


if __name__ == '__main__':
    main()
