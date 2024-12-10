# Importar el módulo tkinter para crear la interfaz gráfica
import tkinter as tk
from tkinter import messagebox
import os
import winsound
from logica_trivia import check_answer  # Cambiar el nombre de importación

# Obtenemos la ruta absoluta del archivo actual usando la variable especial __file__
ruta_absoluta = os.path.abspath(__file__)
# Obtenemos el directorio actual usando la función os.path.dirname
directorio_actual = os.path.dirname(ruta_absoluta)
print(f"Ruta absoluta del archivo: {ruta_absoluta}")
print(f"Directorio actual: {directorio_actual}")

# Función para manejar la respuesta del usuario
def manejar_respuesta(opcion, opcion_correcta, cara_feliz, cara_triste):
    if check_answer(opcion, opcion_correcta):
        # Mostrar cara feliz
        etiqueta_cara.config(image=cara_feliz)
        winsound.PlaySound(os.path.join(directorio_actual, 'resources', 'audio', 'sonido_correcto.wav'), winsound.SND_FILENAME)  # Sonido correcto
        messagebox.showinfo("¡Correcto!", "¡Respuesta correcta!")
    else:
        # Mostrar cara triste
        etiqueta_cara.config(image=cara_triste)
        winsound.PlaySound(os.path.join(directorio_actual, 'resources', 'audio', 'sonido_incorrecto.wav'), winsound.SND_FILENAME)  # Sonido incorrecto
        messagebox.showwarning("Incorrecto", "Respuesta incorrecta")

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Trivia de Ciencias Naturales")

# Pregunta de la trivia
pregunta = "¿Cuál es la flor que se ve?"

# Mostrar la pregunta en la interfaz
etiqueta_pregunta = tk.Label(ventana_principal, text=pregunta, font=("Arial", 16))
etiqueta_pregunta.pack()

# Cargar imágenes
imagen_flor = tk.PhotoImage(file=os.path.join(directorio_actual, "resources", "images", "plant.png"))  # Cambia a la imagen de la flor
cara_feliz = tk.PhotoImage(file=os.path.join(directorio_actual, "resources", "images", "cara_feliz.png"))
cara_triste = tk.PhotoImage(file=os.path.join(directorio_actual, "resources", "images", "cara_triste.png"))

# Mostrar imagen de la flor
etiqueta_imagen = tk.Label(ventana_principal, image=imagen_flor)
etiqueta_imagen.pack()

# Mostrar imagen de la cara (inicialmente vacía)
etiqueta_cara = tk.Label(ventana_principal)
etiqueta_cara.pack()

# Definir opciones de respuesta
opcion_correcta = "Orquídea"  # Cambiado a orquídea
opcion_1 = "Flor de loto"
opcion_2 = "Flor de hibisco"
opcion_3 = "Orquídea"

# Crear botones de opciones
boton_1 = tk.Button(ventana_principal, text=opcion_1, command=lambda: manejar_respuesta(opcion_1, opcion_correcta, cara_feliz, cara_triste))
boton_1.pack()

boton_2 = tk.Button(ventana_principal, text=opcion_2, command=lambda: manejar_respuesta(opcion_2, opcion_correcta, cara_feliz, cara_triste))
boton_2.pack()

boton_3 = tk.Button(ventana_principal, text=opcion_3, command=lambda: manejar_respuesta(opcion_3, opcion_correcta, cara_feliz, cara_triste))
boton_3.pack()

# Iniciar el loop de la ventana
ventana_principal.mainloop()
