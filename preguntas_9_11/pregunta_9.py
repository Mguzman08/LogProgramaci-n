# Conversión de Base Numérica

numero = int(input("Ingrese un número decimal: "))
base = int(input("Ingrese la base destino (2, 8 o 16): "))

# Validación de base
if base not in [2, 8, 16]:
    print("Error: Base no válida. Solo se permite 2, 8 o 16.")
else:
    resultado = ""

    # Caso especial: número 0
    if numero == 0:
        resultado = "0"
    else:
        while numero > 0:
            residuo = numero % base

            # Conversión para hexadecimal
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