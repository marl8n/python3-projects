
class Objeto:
    _NAME = ['MARLON','IVAN']

    def __init__(self, chosen_name):
        self._chosen_name = chosen_name

    def first_name(self):
        self._chosen_name = True
        self.display_name()

    def secund_name(self):
        self._chosen_name = False
        self.display_name()

    def display_name(self):
        if self._chosen_name:
            print(self._NAME[0])
        else:
            print(self._NAME[1])


def run():
    objeto = Objeto(chosen_name=True)

    while True:
        command = input('''
        
        [m]arlon
        [i]van
        [s]alir
                ''')

        if command == 'm':
            objeto.first_name()
        elif command == 'i':
            objeto.secund_name()
        else:
            break




if __name__ == '__main__':
    run()
