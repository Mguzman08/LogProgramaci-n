"""Pruebas unitarias para validar la actualización de la tabla de fútbol."""

import unittest
from Exercise5 import actualizar_y_ordenar_liga


class TestLigaFutbol(unittest.TestCase):

    def test_actualizacion_y_ordenamiento_estandar(self):
        # Datos iniciales base
        equipos = {
            "LAL": {"pj": 0, "pg": 0, "pe": 0, "gf": 0, "gc": 0, "pts": 0},
            "MIL": {"pj": 0, "pg": 0, "pe": 0, "gf": 0, "gc": 0, "pts": 0},
        }
        # Partido jugado
        partidos = [
            {"local": "LAL", "goles_local": 3, "visitante": "MIL", "goles_visitante": 1}
        ]
        
        tabla = actualizar_y_ordenar_liga(equipos, partidos)
        
        # Validaciones de posiciones y puntos
        self.assertEqual(tabla[0]["codigo"], "LAL")
        self.assertEqual(tabla[0]["pts"], 3)
        self.assertEqual(tabla[1]["codigo"], "MIL")
        self.assertEqual(tabla[1]["pts"], 0)

    def test_desempate_por_goles(self):
        # Dos equipos que ganan y quedan con 3 puntos cada uno
        equipos = {
            "TEAM_A": {"pj": 0, "pg": 0, "pe": 0, "gf": 0, "gc": 0, "pts": 0},
            "TEAM_B": {"pj": 0, "pg": 0, "pe": 0, "gf": 0, "gc": 0, "pts": 0},
        }
        partidos = [
            {"local": "TEAM_A", "goles_local": 1, "visitante": "TEAM_B", "goles_visitante": 5}
        ]
        
        tabla = actualizar_y_ordenar_liga(equipos, partidos)
        
        # TEAM_B ganó 5-1, tiene diferencia +4. Debe ir de primero.
        self.assertEqual(tabla[0]["codigo"], "TEAM_B")


if __name__ == "__main__":
    unittest.main()