"""Módulo para la calificación y análisis estadístico de exámenes de admisión."""

from typing import Any, Dict, List


def procesar_examen_admision(
    plantilla: List[int], estudiantes: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """Evalúa los exámenes de N estudiantes y genera métricas globales.

    Args:
        plantilla (List[int]): Lista con las 60 respuestas correctas (1 al 5).
        estudiantes (List[Dict]): Datos de alumnos con credencial y respuestas.

    Returns:
        Dict[str, Any]: Resultados resumidos del examen.
    """
    if not estudiantes:
        return {
            "estudiantes": [],
            "promedio_matematica": 0.0,
            "promedio_verbal": 0.0,
            "promedio_total": 0.0,
            "superan_promedio": [],
            "mejor_estudiante": {},
        }

    # Separar la plantilla en los dos componentes del examen
    correctas_mat = plantilla[:30]
    correctas_verb = plantilla[30:]

    resultados_estudiantes = []
    total_mat_global = 0
    total_verb_global = 0

    max_puntaje = -1
    mejor_credencial = ""

    # Procesar cada estudiante uno a uno
    for est in estudiantes:
        credencial = est["credencial"]
        resp_mat = est["matematica"]
        resp_verb = est["verbal"]

        # Calcular aciertos emparejando con zip()
        puntos_mat = sum(1 for r, c in zip(resp_mat, correctas_mat) if r == c)
        puntos_verb = sum(1 for r, c in zip(resp_verb, correctas_verb) if r == c)
        puntos_total = puntos_mat + puntos_verb

        # Acumular para los promedios globales
        total_mat_global += puntos_mat
        total_verb_global += puntos_verb

        # Validar si es el mayor puntaje registrado
        if puntos_total > max_puntaje:
            max_puntaje = puntos_total
            mejor_credencial = credencial

        resultados_estudiantes.append(
            {
                "credencial": credencial,
                "puntaje_matematica": puntos_mat,
                "puntaje_verbal": puntos_verb,
                "puntaje_total": puntos_total,
            }
        )

    # Calcular promedios globales
    num_estudiantes = len(estudiantes)
    prom_mat = total_mat_global / num_estudiantes
    prom_verb = total_verb_global / num_estudiantes
    prom_total = (total_mat_global + total_verb_global) / num_estudiantes

    # Filtrar estudiantes con puntaje superior o igual al promedio total
    superan_prom = [
        {"credencial": e["credencial"], "puntaje_total": e["puntaje_total"]}
        for e in resultados_estudiantes
        if e["puntaje_total"] >= prom_total
    ]

    return {
        "estudiantes": resultados_estudiantes,
        "promedio_matematica": round(prom_mat, 2),
        "promedio_verbal": round(prom_verb, 2),
        "promedio_total": round(prom_total, 2),
        "superan_promedio": superan_prom,
        "mejor_estudiante": {
            "credencial": mejor_credencial,
            "puntaje_total": max_puntaje,
        },
    }