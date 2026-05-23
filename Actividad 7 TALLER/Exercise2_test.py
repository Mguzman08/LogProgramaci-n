import unittest
# Importamos las funciones reales del ejercicio del determinante
from Exercise2 import fill_matrix, calcular_determinante 

# La clase DEBE empezar con "Test"
class TestMatrizDeterminante(unittest.TestCase):

    # Cada función de prueba DEBE empezar con "test_" en minúsculas
    def test_matriz_1x1(self):
        matriz = [[7]]
        self.assertEqual(calcular_determinante(matriz), 7)

    def test_matriz_2x2(self):
        matriz = [[4, 3], 
                  [1, 2]]
        # (4 * 2) - (3 * 1) = 8 - 3 = 5
        self.assertEqual(calcular_determinante(matriz), 5)

    def test_llenar_matriz_dimensiones(self):
        # Validamos que fill_matrix cree las dimensiones correctas NxN
        matriz = fill_matrix(3)
        self.assertEqual(len(matriz), 3)
        self.assertEqual(len(matriz[0]), 3)

if __name__ == "__main__":
    unittest.main()