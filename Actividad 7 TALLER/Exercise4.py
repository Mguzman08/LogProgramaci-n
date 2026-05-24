"""Módulo para el análisis financiero de matrices de ventas por vendedor y año."""

from typing import Any, Dict, List


def analizar_matriz_ventas(matriz: List[List[float]]) -> Dict[str, Any]:
    """Calcula las ventas acumuladas por vendedor, por año y el total global.

    Args:
        matriz (List[List[float]]): Matriz N x M (Filas: Vendedores, Columnas: Años).

    Returns:
        Dict[str, Any]: Diccionario con los vectores de resultados y el gran total.
    """
    # Caso base por si la matriz ingresada está vacía
    if not matriz or not matriz[0]:
        return {"ventas_vendedor": [], "ventas_ano": [], "gran_total": 0.0}

    num_vendedores = len(matriz)
    num_anos = len(matriz[0])

    # 1. Total de ventas de cada vendedor (Suma por Filas)
    ventas_vendedor = [sum(vendedor) for vendedor in matriz]

    # 2. Total de ventas en cada año (Suma por Columnas)
    ventas_ano = [0.0] * num_anos
    for i in range(num_vendedores):
        for j in range(num_anos):
            ventas_ano[j] += matriz[i][j]

    # 3. Gran total de ventas de la empresa
    gran_total = sum(ventas_vendedor)

    return {
        "ventas_vendedor": ventas_vendedor,
        "ventas_ano": ventas_ano,
        "gran_total": gran_total,
    }