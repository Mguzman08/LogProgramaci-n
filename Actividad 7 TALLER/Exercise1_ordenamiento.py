"""Pruebas unitarias para el módulo de ordenamiento."""

import unittest
from Exercise1 import ordenar_burbuja_descendente, generar_arreglo_aleatorio


class TestOrdenamientoBurbuja(unittest.TestCase):

    def test_ordenamiento_estandar(self):
        """Prueba con una lista desordenada común."""
        caso = [15, 3, 28, 40, 1]
        resultado = ordenar_burbuja_descendente(caso)
        self.assertEqual(resultado, [40, 28, 15, 3, 1])

    def test_lista_ya_ordenada(self):
        """Prueba con una lista que ya está ordenada de mayor a menor."""
        caso = [50, 40, 30, 20]
        resultado = ordenar_burbuja_descendente(caso)
        self.assertEqual(resultado, [50, 40, 30, 20])

    def test_lista_vacia_y_un_elemento(self):
        """Prueba casos base con listas vacías o de un único elemento."""
        self.assertEqual(ordenar_burbuja_descendente([]), [])
        self.assertEqual(ordenar_burbuja_descendente([7]), [7])

    def test_numeros_negativos(self):
        """Prueba que el algoritmo gestione correctamente números negativos."""
        caso = [-5, 10, 0, -20, 5]
        resultado = ordenar_burbuja_descendente(caso)
        self.assertEqual(resultado, [10, 5, 0, -5, -20])

    def test_generacion_tamano(self):
        """Prueba que el generador cree la cantidad correcta de elementos."""
        arreglo = generar_arreglo_aleatorio(15)
        self.assertEqual(len(arreglo), 15)


if __name__ == "__main__":
    unittest.main()