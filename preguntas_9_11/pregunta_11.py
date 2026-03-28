# Analisis de calificaciones

N = int(input("Ingrese la cantidad de estudiantes: "))

suma = 0
aprobados = 0
reprobados = 0

# Inicialización con primera nota
nota = float(input("Ingrese la calificación del estudiante 1: "))
mayor = nota
menor = nota
suma += nota

if nota >= 60:
    aprobados += 1
else:
    reprobados += 1

# Ciclo para el resto
for i in range(2, N + 1):
    nota = float(input(f"Ingrese la calificación del estudiante {i}: "))
    
    suma += nota

    if nota >= 60:
        aprobados += 1
    else:
        reprobados += 1

    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

promedio = suma / N

print("Promedio:", promedio)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Calificación más alta:", mayor)
print("Calificación más baja:", menor)