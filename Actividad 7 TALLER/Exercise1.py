"""Módulo para la generación y ordenamiento de arreglos usando el metodo burbuja Burbuja."""

import random
from typing import List


def generar_arreglo_aleatorio(tamano: int) -> List[int]:
    """Genera un arreglo de N elementos con números enteros aleatorios.

    Args:
        tamano (int): Cantidad de elementos (N).

    Returns:
        List[int]: Lista con elementos aleatorios entre 1 y 100.
    """
    if tamano < 0:
        raise ValueError("El tamaño del arreglo no puede ser negativo.")
    return [random.randint(1, 100) for _ in range(tamano)]


def ordenar_burbuja_descendente(arreglo: List[int]) -> List[int]:
    """Ordena un arreglo de mayor a menor usando el método burbuja.

    Args:
        arreglo (List[int]): Lista original de números enteros.

    Returns:
        List[int]: Nueva lista ordenada de mayor a menor.
    """
    # Copiamos la lista para mantener la función pura y no alterar la original
    lista = arreglo.copy()
    n = len(lista)

    # Algoritmo de burbuja optimizado con bandera de intercambio
    for i in range(n):
        intercambio = False
        # El subíndice (n - i - 1) evita revisar los elementos ya ordenados
        for j in range(0, n - i - 1):
            # Condición para ordenar de MAYOR a MENOR (<)
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True

        # Si no hubo intercambios en la pasada, el arreglo ya está ordenado
        if not intercambio:
            break

    return lista


if __name__ == "__main__":
    # Ejemplo de ejecución
    N = 10
    arreglo_original = generar_arreglo_aleatorio(N)
    arreglo_ordenado = ordenar_burbuja_descendente(arreglo_original)

    print(f"Arreglo Original: {arreglo_original}")
    print(f"Arreglo Ordenado (Mayor a Menor): {arreglo_ordenado}")

