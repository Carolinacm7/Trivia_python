import tkinter as tk
import os
from tkinter import messagebox
from PIL import Image, ImageTk  # Para manejar imágenes
from playsound import playsound  # Para reproducir archivos mp3

# Obtenemos la ruta absoluta del archivo actual usando la variable especial __file__
ruta_absoluta = os.path.abspath(__file__)
# Obtenemos el directorio actual usando la función os.path.dirname
directorio_actual = os.path.dirname(ruta_absoluta)