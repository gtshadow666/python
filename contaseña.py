import random
import string

def generar_contraseña(longitud):
    if longitud < 4:
        print("La longitud mínima recomendada es 4.")
        return None

    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(caracteres) for _ in range(longitud))

while True:
    # Pedir al usuario la longitud de la contraseña
    try:
        longitud = int(input("Introduce la longitud de la contraseña: "))
        contraseña_generada = generar_contraseña(longitud)
        if contraseña_generada:
            print("Tu contraseña generada es:", contraseña_generada)
    except ValueError:
        print("Por favor, introduce un número válido.")