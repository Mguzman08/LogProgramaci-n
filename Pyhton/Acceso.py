"""Creacion de usuario, Contraseña y inicio de sesión
"""

import re
usuarios_registrados = {}

"""Especificaciones para la contraseña"""

def validar_contraseña(password):
    patron = r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$"

    if re.search(patron, password):
        return True
    else:
        return False
"""Creación de usuario"""

USERNAME = input("Cree su usuario: ")
PASSWORD = input("Cree su contraseña: ")

while not validar_contraseña(PASSWORD):
    print("Contraseña debil")
    print("""
        Debe contener
        Mayusculas
        Numeros
        Caracteres Especiales
        Minimo 8 caracteres  
            """)
    PASSWORD = input("Intenete nuevamente: ")

print(f"Datos guardados {USERNAME}")

usuarios_registrados[USERNAME] = PASSWORD

"""Inicio de Sesión"""

attempts = 0

USERNAME = input("Ingrese su usuario: ")
PASSWORD = input("Ingrese su contraseña: ")

if USERNAME in usuarios_registrados and usuarios_registrados[USERNAME] == PASSWORD:
    print("Bienvenido")

else:
    attempts += 1
    while attempts < 3:
        print('Los datos ingresados son incorrectos. Intentelo nuevamenete')

        USERNAME = input('Ingresa su nombre de usuario: ')
        PASSWORD = input("Ingrese su password :")

        if PASSWORD == PASSWORD and USERNAME == USERNAME:
            attempts = 0
            print(f'Bienvenido al sistema {USERNAME}')
            break

        attempts = attempts + 1

    else:
        print("su cuenta ha sido bloqueada")
