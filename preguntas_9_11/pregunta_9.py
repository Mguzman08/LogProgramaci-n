# Conversión de Base Numérica

numero = int(input("Ingrese un número decimal: "))
base = int(input("Ingrese la base destino (2, 8 o 16): "))

resultado = ""

while numero > 0:
    residuo = numero % base

    # Para hexadecimal
    if residuo == 10:
        digito = "A"
    elif residuo == 11:
        digito = "B"
    elif residuo == 12:
        digito = "C"
    elif residuo == 13:
        digito = "D"
    elif residuo == 14:
        digito = "E"
    elif residuo == 15:
        digito = "F"
    else:
        digito = str(residuo)

    resultado = digito + resultado
    numero = numero // base

print("Resultado:", resultado)