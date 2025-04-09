import tkinter as tk
import random

class Ahorcado(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Juego del Ahorcado")
        self.geometry("400x400")
        self.resizable(False, False)

        # Diccionario de palabras por dificultad
        self.palabras = {
            "fácil": ["gato", "sol", "casa", "pan", "luz"],
            "normal": ["ratón", "ventana", "mesa", "perro", "camisa"],
            "difícil": ["astronauta", "murciélago", "elefante", "psicólogo", "anfitrión"]
        }

        # Variables
        self.dificultad = tk.StringVar(value="fácil")
        self.usar_pistas = tk.BooleanVar()
        self.palabra = ""
        self.letras_adivinadas = []
        self.intentos = 6

        # Interfaz
        self.crear_widgets()

    def crear_widgets(self):
        # Selección de dificultad
        tk.Label(self, text="Selecciona la dificultad:").pack()
        for nivel in ["fácil", "normal", "difícil"]:
            tk.Radiobutton(self, text=nivel.capitalize(), variable=self.dificultad, value=nivel).pack

        # Botón para iniciar el juego
        tk.Button(self, text="Empezar juego", command=self.iniciar_juego).pack(pady=10)

        # Área de juego
        self.label_palabra = tk.Label(self, text="_ _ _ _", font=("Courier", 24))
        self.label_palabra.pack(pady=10)

        self.label_info = tk.Label(self, text="Intentos restantes: 6")
        self.label_info.pack()

        # Entrada de letra
        self.entry_letra = tk.Entry(self, width=5, font=("Courier", 18))
        self.entry_letra.pack(pady=5)

        self.boton_probar = tk.Button(self, text="Probar letra", command=self.probar_letra, state=tk.DISABLED)
        self.boton_probar.pack()

    def iniciar_juego(self):
        # Reiniciar valores
        self.palabra = random.choice(self.palabras[self.dificultad.get()])
        self.letras_adivinadas = []
        self.intentos = 6

        # Actualizar interfaz
        self.mostrar_palabra()
        self.label_info.config(text="Intentos restantes: 6")
        self.entry_letra.delete(0, tk.END)
        self.boton_probar.config(state=tk.NORMAL)

    def mostrar_palabra(self):
        texto_mostrado = " ".join([letra if letra in self.letras_adivinadas else "_" for letra in self.palabra])
        self.label_palabra.config(text=texto_mostrado)

    def probar_letra(self):
        letra = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)

        if not letra.isalpha() or len(letra) != 1:
            self.label_info.config(text="Introduce solo una letra.")
            return

        if letra in self.letras_adivinadas:
            self.label_info.config(text="Ya intentaste esa letra.")
            return

        self.letras_adivinadas.append(letra)

        if letra in self.palabra:
            self.label_info.config(text="¡Bien!")
        else:
            self.intentos -= 1
            self.label_info.config(text=f"Letra incorrecta. Intentos restantes: {self.intentos}")

        self.mostrar_palabra()
        self.comprobar_estado()

    def comprobar_estado(self):
        if all(letra in self.letras_adivinadas for letra in self.palabra):
            self.label_info.config(text="¡Ganaste! 🎉")
            self.boton_probar.config(state=tk.DISABLED)
        elif self.intentos <= 0:
            self.label_info.config(text=f"¡Perdiste! La palabra era: {self.palabra}")
            self.label_palabra.config(text=self.palabra)
            self.boton_probar.config(state=tk.DISABLED)

# Ejecutar el juego
if __name__ == "__main__":
    juego = Ahorcado()
    juego.mainloop()
