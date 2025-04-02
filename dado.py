# Importar todos los elementos de tkinter (para widgets básicos)
from tkinter import *
# Importar tkinter con alias 'tk' (buena práctica para evitar conflictos)
import tkinter as tk
# De PIL (Pillow) importamos las clases para manejar imágenes
from PIL import ImageTk, Image 
# Módulo para generación de números aleatorios
import random
# Módulo para pausas/retrasos (usado en la animación)
import time

class Aplicacion:
    def __init__(self, root):
        # Constructor: inicializa la aplicación
        self.root = root
        self.root.title("DADO GIRANDO")  # Título de la ventana
        self.root.geometry("300x300")   # Tamaño inicial (ancho x alto)
        # Label vacío donde mostraremos la imagen del dado
        self.label_imagen = tk.Label(root)
        self.label_imagen.pack()  # Lo empacamos en la ventana
        # Creamos un botón con texto "TIRAR" que ejecutará self.generar al clickear
        self.boton = tk.Button(root, text="TIRAR", anchor=S,command=self.generar)
        # Empacamos el botón con un margen vertical de 10 píxeles
        self.boton.pack(pady=10)
        
        
        
        # Diccionario para almacenar las imágenes precargadas
        self.imagenes = {}
        # Precargamos las 6 imágenes del dado (1.jpg a 6.jpg)
        for i in range(1, 7):
            try:
                # Ruta dinámica según el número del dado
                ruta = f"recursos/{i}.jpg"
                # Abrir la imagen y redimensionar a 150x150 (opcional)
                img = Image.open(ruta).resize((150, 150))
                # Convertir a formato compatible con Tkinter y guardar en el diccionario
                self.imagenes[i] = ImageTk.PhotoImage(img)
            except:
                # Mensaje si hay error al cargar una imagen
                print(f"Error al cargar: {ruta}")
    
    def generar(self):
        # Deshabilitamos el botón durante la animación para evitar clicks múltiples
        self.boton.config(state=tk.DISABLED)

        # Animación: 20 cambios rápidos de imagen (simula giro)
        for _ in range(20):
            # Elegimos un número de dado aleatorio temporal
            num_temp = random.randint(1, 6)
            # Actualizamos la imagen en el Label
            self.label_imagen.config(image=self.imagenes[num_temp])
            # Mantenemos una referencia para evitar garbage collection
            self.label_imagen.image = self.imagenes[num_temp]
            # Forzamos actualización inmediata de la interfaz
            self.root.update()
            # Pequeña pausa para controlar la velocidad de la animación (50ms)
            time.sleep(0.05)
        
        # Al terminar la animación, elegimos el resultado final
        numero_final = random.randint(1, 6)
        # Mostramos la imagen correspondiente al resultado
        self.label_imagen.config(image=self.imagenes[numero_final])
        # Rehabilitamos el botón para nuevos lanzamientos
        self.boton.config(state=tk.NORMAL)

# Bloque principal: solo se ejecuta si el script es el programa principal
if __name__ == "__main__":
    root = tk.Tk()  # Creamos la ventana principal
    app = Aplicacion(root)  # Instanciamos nuestra aplicación
    root.mainloop()  # Iniciamos el bucle principal de eventos
