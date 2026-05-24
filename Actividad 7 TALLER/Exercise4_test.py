"""Pruebas unitarias para validar los cálculos matriciales de ventas."""

import unittest
from Exercise4 import analizar_matriz_ventas


class TestAnalisisVentas(unittest.TestCase):

    def test_matriz_estandar(self):
        matriz = [
            [10.0, 20.0, 30.0],
            [5.0, 15.0, 25.0]
        ]
        resultado = analizar_matriz_ventas(matriz)
        
        self.assertEqual(resultado["ventas_vendedor"], [60.0, 45.0])
        self.assertEqual(resultado["ventas_ano"], [15.0, 35.0, 55.0])
        self.assertEqual(resultado["gran_total"], 105.0)

    def test_matriz_vacia(self):
        resultado = analizar_matriz_ventas([])
        self.assertEqual(resultado["gran_total"], 0.0)
        self.assertEqual(resultado["ventas_vendedor"], [])


if __name__ == "__main__":
    unittest.main()