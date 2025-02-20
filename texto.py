import string
import os
from tkinter import filedialog

DATA_DIR = "data"
ALPHABET_FILE = os.path.join(DATA_DIR, "texto.txt")

# Crear el directorio si no existe
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


def guardar_texto(texto, alfabeto):
    with open(ALPHABET_FILE, 'w', encoding='utf-8') as archivo:
        if not validar_texto(texto, alfabeto):
            raise ValueError("El texto contiene caracteres no permitidos.")
        archivo.write(texto)


def cargar_texto(alfabeto):
    with open(ALPHABET_FILE, 'r', encoding='utf-8') as archivo:
        if not validar_texto(archivo.read(), alfabeto):
            raise ValueError("El texto contiene caracteres no permitidos.")
        return archivo.read()


def cambiar_texto(alfabeto):
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt")]
    )

    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as archivo:
                nuevo_texto = archivo.read()
                guardar_texto(nuevo_texto, alfabeto)
                return nuevo_texto
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            raise e
    else:
        print("No se seleccionó ningún archivo.")


def validar_texto(texto, alfabeto: list | str) -> bool:
    if not isinstance(alfabeto, str):
        alfabeto = ''.join(alfabeto).lower() + ' '
    else:
        alfabeto = alfabeto.lower() + ' '
    texto = texto.lower()
    for caracter in texto:
        if caracter not in alfabeto:
            return False
    return True
