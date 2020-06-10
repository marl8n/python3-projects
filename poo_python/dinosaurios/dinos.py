
class Dinosaurio:
    dino_dibujo = {
    t: '''
                            . - ~ ~ ~ - .
      ..     _      .-~               ~-.
     //|     \ `..~                      `.
    || |      }  }              /       \  \
(\   \\ \~^..'                 |         }  \
 \`.-~  o      /       }       |        /    \
 (__          |       /        |       /      `.
  `- - ~ ~ -._|      /_ - ~ ~ ^|      /- _      `.
              |     /          |     /     ~-.     ~- _
              |_____|          |_____|         ~ - . _ _~_-_
        ''',
        a: '''
                             /~~~~~~~~~~~~\_
 _+=+_             _[~  /~~~~~~~~~~~~\_
{""|""}         [~~~    [~   /~~~~~~~~~\_
 """:-'~[~[~"~[~  ((++     [~  _/~~~~~~~~\_
      '=_   [    ,==, ((++    [    /~~~~~~~\-~~~-.
         ~-_ _=+-(   )/   ((++  .~~~.[~~~~(  {@} \`.
                 /   }\ /     (     }     (   .   ''}
                (  .+   \ /  //     )    / .,  """"/
                \\  \     \ (   .+~~\_  /.= /'""""
                <"_V_">      \\  \    ~~~~~~\\  \
                              \\  \          \\  \
                              <"_V_">        <"_V_">
        '''

    }

    def __init__(self, poder, dibujo, proteccion):
        self.poder = poder
        self.dibujo = dibujo
        self.proteccion = proteccion

    def _print_dino(self, dibujo):
        print(dino_dibujo)


def main():
    dino_eleccion = input('''

    Que dinosaurio quiere?
    [t]riceratops

    ''')


if __name__ == '__main__':
    main()
