# Cálculo de Números Primos

M = int(input("Ingrese un número entero positivo: "))

suma = 0
contador = 0

for i in range(2, M + 1):
    es_primo = True

    for j in range(2, int(i**0.5) + 1):  # optimización
        if i % j == 0:
            es_primo = False
            break

    if es_primo:
        print(i)
        suma += i
        contador += 1

print("Suma de primos:", suma)
print("Cantidad de primos:", contador)