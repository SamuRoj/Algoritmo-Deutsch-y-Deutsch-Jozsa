import unittest
import Deutsch
import DeutschJozsa


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print("Resultados Experimento de Deutsch")
        self.assertEqual(Deutsch.Pruebas(), [{'00': 1000}, {'01': 1000}, {'10': 1000}, {'11': 1000}, {'00': 1000}, {'01': 1000}, {'11': 1000}, {'10': 1000}, {'01': 1000}, {'00': 1000}, {'10': 1000}, {'11': 1000}, {'01': 1000}, {'00': 1000}, {'11': 1000}, {'10': 1000}, 'Constante', 'Balanceada', 'Balanceada', 'Constante'])
        print("Resultados Experimento de Deutsch-Jozsa")
        self.assertEqual(DeutschJozsa.Pruebas(), [{'00000': 1000}, {'00010': 1000}, {'00100': 1000}, {'10000': 1000}, {'00000': 1000}, {'00010': 1000}, {'00100': 1000}, {'10001': 1000}, {'00000': 1000}, {'10000': 1000}, {'00010': 1000}, {'01101': 1000}, {'00000': 1000}, {'10000': 1000}, {'01000': 1000}, {'00101': 1000}, 'Constante', 'Balanceada', 'Balanceada', 'Balanceada'])


if __name__ == '__main__':
    unittest.main()
