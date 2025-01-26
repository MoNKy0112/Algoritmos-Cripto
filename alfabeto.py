import os

DATA_DIR = "data"
ALPHABET_FILE = os.path.join(DATA_DIR, "alfabeto_personalizado.txt")

# Crear el directorio si no existe
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


def guardar_alfabeto(alphabet):
    with open(ALPHABET_FILE, 'w', encoding='utf-8') as file:
        for letter in alphabet:
            file.write(letter + '\n')

    print("Alfabeto cambiado con éxito.")


def cargar_alfabeto():
    if os.path.exists(ALPHABET_FILE):
        with open(ALPHABET_FILE, 'r', encoding='utf-8') as file:
            print("Alfabeto cargado con éxito.")
            return [line.strip() for line in file]
    return None


def cambiar_alfabeto():
    from tkinter import filedialog
    new_alphabet = []
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt")]
    )

    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    new_alphabet.append(line.strip())
            guardar_alfabeto(new_alphabet)
            print("Alfabeto cambiado con éxito.2")
            return new_alphabet
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    else:
        print("No se seleccionó ningún archivo.")
