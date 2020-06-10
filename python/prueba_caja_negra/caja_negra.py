import unittest

class CajaNegraTest(unittest.TestCase):
    
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num2)

        self.assertEqual(resultado, 15)



if __name__ == '__main__':
    unitttest.main()
