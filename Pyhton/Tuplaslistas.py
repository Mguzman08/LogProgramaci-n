#tuple = (10, object)

#lista = [a, b, True]

#diccionario = ("clave": 10, "valor": 5)

#diccionario = ("clave": 10, "valor": 5)


# Definimos la función
def calcular_imc(peso, altura):
    resultado = peso / (altura ** 2)


# Usamos la función en el programa principal
mi_peso = 70
mi_altura = 1.75

# Guardamos lo que el return nos devuelve en una variable
indice = calcular_imc(mi_peso, mi_altura)

print(f"Tu IMC es: {indice:.2f}")

