"""Módulo para la gestión y ordenamiento de tablas de posiciones de fútbol."""

from typing import Any, Dict, List


def actualizar_y_ordenar_liga(
    equipos: Dict[str, Dict[str, int]], partidos: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Actualiza las estadísticas de la liga y ordena la tabla de posiciones.

    Args:
        equipos (Dict): Diccionario con los datos históricos de los equipos.
        partidos (List): Lista de los encuentros disputados en la última fecha.

    Returns:
        List[Dict]: Tabla final de posiciones ordenada descendentemente.
    """
    # 1. Procesar y acumular los resultados de los partidos de la fecha
    for encuentro in partidos:
        local = encuentro["local"]
        goles_local = encuentro["goles_local"]
        visitante = encuentro["visitante"]
        goles_visitante = encuentro["goles_visitante"]

        # Actualizar partidos jugados y goles en el diccionario global
        equipos[local]["pj"] += 1
        equipos[visitante]["pj"] += 1
        equipos[local]["gf"] += goles_local
        equipos[local]["gc"] += goles_visitante
        equipos[visitante]["gf"] += goles_visitante
        equipos[visitante]["gc"] += goles_local

        # Evaluar distribución de puntos por resultado del partido
        if goles_local > goles_visitante:
            equipos[local]["pg"] += 1
            equipos[local]["pts"] += 3
        elif goles_visitante > goles_local:
            equipos[visitante]["pg"] += 1
            equipos[visitante]["pts"] += 3
        else:
            equipos[local]["pe"] += 1
            equipos[visitante]["pe"] += 1
            equipos[local]["pts"] += 1
            equipos[visitante]["pts"] += 1

    # Convertir el diccionario a una lista plana para poder aplicar el ordenamiento
    tabla_posiciones = []
    for codigo, datos in equipos.items():
        registro = {"codigo": codigo, **datos}
        tabla_posiciones.append(registro)

    # 2. Ordenamiento por Burbuja con doble criterio de desempate
    n = len(tabla_posiciones)
    for i in range(n):
        intercambio = False
        for j in range(0, n - i - 1):
            # Calcular diferencias de goles actuales para el desempate
            dif_j = tabla_posiciones[j]["gf"] - tabla_posiciones[j]["gc"]
            dif_sig = tabla_posiciones[j + 1]["gf"] - tabla_posiciones[j + 1]["gc"]

            hacer_intercambio = False

            # Criterio principal: Menos puntos que el siguiente
            if tabla_posiciones[j]["pts"] < tabla_posiciones[j + 1]["pts"]:
                hacer_intercambio = True
            
            # Criterio secundario: Mismos puntos pero menor diferencia de goles
            elif tabla_posiciones[j]["pts"] == tabla_posiciones[j + 1]["pts"]:
                if dif_j < dif_sig:
                    hacer_intercambio = True

            # Ejecutar el intercambio físico de posiciones en la lista
            if hacer_intercambio:
                tabla_posiciones[j], tabla_posiciones[j + 1] = (
                    tabla_posiciones[j + 1],
                    tabla_posiciones[j],
                )
                intercambio = True

        # Si no hubo cambios en toda la pasada, la lista ya está ordenada
        if not intercambio:
            break

    return tabla_posiciones
