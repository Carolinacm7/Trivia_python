import tkinter as tk
from tkinter import messagebox
import os
import winsound
from PIL import Image, ImageTk
from logica_trivia import check_answer

# Obtenemos la ruta absoluta del archivo actual usando la variable especial __file__
ruta_absoluta = os.path.abspath(__file__)
# Obtenemos el directorio actual usando la función os.path.dirname
directorio_actual = os.path.dirname(ruta_absoluta)
#estilos boton emergente 
estilo_boton_cerrar = {
    "font": ("Arial", 14, "bold"),  
    "bg": "black",  
    "fg": "white",  
    "activebackground": "purple", 
    "activeforeground": "white",  
    "relief": "groove", 
    "bd": 2,  
    "width": 20, 
    "pady": 10  
}
# Función para manejar la respuesta
def verificar_respuesta(opcion_seleccionada, opcion_correcta):
    #si no responde antes de dar verificar 
    if opcion_seleccionada is None:
        messagebox.showwarning("Seleccionar opción", "Por favor, selecciona una opción antes de verificar")
        return
    #si responde de manera correcta 
    if check_answer(opcion_seleccionada, opcion_correcta):
        mensaje = "¡Respuesta correcta!"
        imagen_respuesta = img_cara_feliz
        winsound.PlaySound(os.path.join(directorio_actual, 'resources', 'audio', 'sonido_correcto.wav'), winsound.SND_FILENAME)
        
        
    #  respuesta incorrecta   
    else:
        mensaje = "¡Respuesta incorrecta! "
        imagen_respuesta = img_cara_triste
        winsound.PlaySound(os.path.join(directorio_actual, 'resources', 'audio', 'sonido_incorrecto.wav'), winsound.SND_FILENAME)
        

    # ventana de respuesta
    ventana_respuesta = tk.Toplevel(ventana_principal)
    ventana_respuesta.title("Resultado")
    ventana_respuesta.geometry("400x350")

    # mensaje en la ventana emergente
    etiqueta_mensaje = tk.Label(ventana_respuesta, text=mensaje, font=("Arial", 14, "bold"))
    etiqueta_mensaje.pack(pady=10)

    #imagen de calificación
    etiqueta_calificacion = tk.Label(ventana_respuesta, image=imagen_respuesta)
    etiqueta_calificacion.pack(pady=10)


    # Botón para cerrar la ventana emergente
    boton_cerrar = tk.Button(ventana_respuesta, text="Cerrar", command=ventana_respuesta.destroy, **estilo_boton_cerrar)
    boton_cerrar.pack(pady=10)

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Trivia de Ciencias Naturales")
ventana_principal.geometry("500x650")  # Tamaño de la ventana

# Pregunta de la trivia
pregunta = "¿Cuál es la flor que se ve?"

# Mostrar la pregunta en la interfaz
etiqueta_pregunta = tk.Label(ventana_principal, text=pregunta, font=("Arial", 16, "bold"), pady=20)
etiqueta_pregunta.pack()

# Cargar y redimensionar la imagen de respuesta usando Pillow
ruta_img_respuesta = os.path.join(directorio_actual, "resources/img/img_respuesta.png")
img_original_respuesta = Image.open(ruta_img_respuesta)
img_redimensionada_respuesta = img_original_respuesta.resize((300, 200))  # Redimensionar a 200x200 píxeles
img_respuesta = ImageTk.PhotoImage(img_redimensionada_respuesta)

# Cargar las imágenes de cara feliz y cara triste
img_cara_feliz_original = Image.open(os.path.join(directorio_actual, "resources/img/img_correcto.png"))
img_cara_feliz_redimensionada = img_cara_feliz_original.resize((200, 200))
img_cara_feliz = ImageTk.PhotoImage(img_cara_feliz_redimensionada)

img_cara_triste_original = Image.open(os.path.join(directorio_actual, "resources/img/img_incorrecto.png"))
img_cara_triste_redimensionada = img_cara_triste_original.resize((200, 200))
img_cara_triste = ImageTk.PhotoImage(img_cara_triste_redimensionada)

# Mostrar imagen de la flor
etiqueta_imagen = tk.Label(ventana_principal, image=img_respuesta)
etiqueta_imagen.pack()

etiqueta_mensaje = tk.Label(ventana_principal, text="Selecciona una opcion y haz clic en verificar.", font=("Arial", 14))
etiqueta_mensaje.pack(pady=10)

# Definir opciones de respuesta
opcion_correcta = "Orquídea"
opcion_1 = "Flor de loto"
opcion_2 = "Flor de hibisco"
opcion_3 = "Orquídea"

# Variable para almacenar la opción seleccionada
opcion_seleccionada = None

# Función para seleccionar la opción
def seleccionar_opcion(opcion):
    global opcion_seleccionada
    opcion_seleccionada = opcion

# estilos botones 
estilo_boton = {
    "font": ("Arial", 14, "bold"),  
    "bg": "white",  
    "fg": "purple",  
    "activebackground": "#EBD2F7",
    "activeforeground": "white", 
    "relief": "ridge",  
    "bd": 5,  
    "width": 24, 
    "pady": 8  
}
estilo_boton_verificar = {
    "font": ("Arial", 14, "bold"),  
    "bg": "black",  
    "fg": "white",  
    "activebackground": "purple", 
    "activeforeground": "white",  
    "relief": "groove", 
    "bd": 2,  
    "width": 25, 
    "pady": 8  
}
# Crear botones de opciones con estilo
boton_1 = tk.Button(ventana_principal, text=opcion_1, command=lambda: seleccionar_opcion(opcion_1), **estilo_boton)
boton_1.pack(pady=10)  # Espacio entre los botones

boton_2 = tk.Button(ventana_principal, text=opcion_2, command=lambda: seleccionar_opcion(opcion_2), **estilo_boton)
boton_2.pack(pady=5)

boton_3 = tk.Button(ventana_principal, text=opcion_3, command=lambda: seleccionar_opcion(opcion_3), **estilo_boton)
boton_3.pack(pady=5)


# Botón de Verificar
boton_verificar = tk.Button(ventana_principal, text="Verificar", command=lambda: verificar_respuesta(opcion_seleccionada, opcion_correcta), **estilo_boton_verificar)
boton_verificar.pack(pady=10)

# Iniciar el loop de la ventana
ventana_principal.mainloop()
