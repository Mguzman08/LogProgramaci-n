"""Módulo para la generación de matrices y cálculo de determinantes."""

import random
from typing import List


def fill_matrix(n: int) -> List[List[int]]:
    """Crea una matriz de N x N con números aleatorios entre 1 y 20.

    Args:
        n (int): Dimensión de la matriz cuadrada.

    Returns:
        List[List[int]]: Matriz poblada.
    """
    if n <= 0:
        raise ValueError("La dimensión N debe ser un entero positivo.")
    return [[random.randint(1, 20) for _ in range(n)] for _ in range(n)]


def obtener_submatriz(
    matriz: List[List[int]], fila: int, columna: int
) -> List[List[int]]:
    """Genera una submatriz eliminando una fila y una columna específicas."""
    return [
        [matriz[i][j] for j in range(len(matriz)) if j != columna]
        for i in range(len(matriz))
        if i != fila
    ]


def calcular_determinante(matriz: List[List[int]]) -> float:
    """Calcula el determinante de una matriz cuadrada de forma recursiva.

    Args:
        matriz (List[List[int]]): Matriz cuadrada N x N.

    Returns:
        float: Valor del determinante.
    """
    n = len(matriz)

    # Caso Base 1: Matriz 1x1
    if n == 1:
        return matriz[0][0]

    # Caso Base 2: Matriz 2x2 (Optimización)
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    # Paso Recursivo (Cofactores de Laplace)
    determinante = 0.0
    for j in range(n):
        submatriz = obtener_submatriz(matriz, 0, j)
        signo = 1 if j % 2 == 0 else -1
        cofactor = calcular_determinante(submatriz)
        determinante += signo * matriz[0][j] * cofactor

    return determinante