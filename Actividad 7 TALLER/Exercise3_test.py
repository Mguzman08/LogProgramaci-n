"""Pruebas unitarias para validar el procesamiento del examen de admisión."""

import unittest
from Exercise3 import procesar_examen_admision


class TestExamenAdmision(unittest.TestCase):

    def test_procesamiento_estandar(self):
        # Plantilla de prueba (60 campos rellenos con 1)
        plantilla = [1] * 60
        
        # Estudiantes simulados
        estudiantes = [
            {"credencial": "U001", "matematica": [1] * 30, "verbal": [1] * 30},  # 60 puntos
            {"credencial": "U002", "matematica": [2] * 30, "verbal": [2] * 30},  # 0 puntos
        ]
        
        resultado = procesar_examen_admision(plantilla, estudiantes)
        
        # Verificaciones
        self.assertEqual(resultado["mejor_estudiante"]["credencial"], "U001")
        self.assertEqual(resultado["mejor_estudiante"]["puntaje_total"], 60)
        self.assertEqual(resultado["promedio_total"], 30.0)
        self.assertEqual(len(resultado["superan_promedio"]), 1)

    def test_caso_vacio(self):
        resultado = procesar_examen_admision([1] * 60, [])
        self.assertEqual(resultado["promedio_total"], 0.0)


if __name__ == "__main__":
    unittest.main()