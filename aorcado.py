import random

def elegir_palabra():
    palabras = ["python", "programacion", "inteligencia", "computadora", "teclado", "ahorcado"]
    return random.choice(palabras)

def mostrar_palabra(palabra, letras_adivinadas):
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra)

def ahorcado():
    palabra = elegir_palabra()
    letras_adivinadas = set()
    intentos = 6
    
    print("\n¡Bienvenido al juego del ahorcado!")
    
    while intentos > 0:
        print("\nPalabra: ", mostrar_palabra(palabra, letras_adivinadas))
        letra = input("Adivina una letra: ").lower()

        if len(letra)!=1 or not letra.isalpha:
            print("Insterte una letra valida y solo una")
            continue
        elif letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta otra vez.")
        elif letra in palabra:
            letras_adivinadas.add(letra)
            print("¡Bien hecho! Esa letra está en la palabra.")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")
        
        if set(palabra) <= letras_adivinadas:
            print("\n ¡Felicidades! Adivinaste la palabra:", palabra)
            break
    else:
        print("\n¡Perdiste! La palabra era:", palabra)

if __name__ == "__main__":
    ahorcado()

