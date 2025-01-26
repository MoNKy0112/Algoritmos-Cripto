import tkinter as tk
from tkinter import Frame, filedialog, simpledialog, messagebox

from alfabeto import cargar_alfabeto, cambiar_alfabeto
from cifrado_cesar import cifrar, descifrar

# Crear una ventana oculta
# root = tk.Tk()
# root.withdraw()  # Oculta la ventana principal
alphabet = cargar_alfabeto()
if alphabet is None:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def cambiar_alfabeto():
#     new_alphabet = []
#     # Abrir el cuadro de diálogo para seleccionar un archivo
#     file_path = filedialog.askopenfilename(
#         title="Selecciona un archivo de texto",
#         filetypes=[("Archivos de texto", "*.txt")]
#     )

#     # Verificar si se seleccionó un archivo
#     if file_path:
#         try:
#             # Abrir el archivo y leer línea por línea
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 for line in file:
#                     # print(line.strip())  # Imprimir la línea sin saltos de línea extra
#                     new_alphabet.append(line.strip())
#             alphabet = new_alphabet
#             return new_alphabet
#         except Exception as e:
#             print(f"Error al leer el archivo: {e}")
#     else:
#         print("No se seleccionó ningún archivo.")


def procesar_opcion(opcion):
    top = tk.Toplevel()
    top.geometry("300x300+500+500")
    listbox = tk.Listbox(top)
    listbox.insert(1, "Cifrado Cesar")
    listbox.insert(2, "Cifrado ...")
    listbox.pack()
    if opcion == "cifrar":

        top.title("Cifrar")

        # Crear una nueva ventana para ingresar datos necesarios segun cifrado
        texto = simpledialog.askstring(
            "Cifrar", "Por favor, ingrese el texto a cifrar:")
        llave = simpledialog.askinteger(
            "Cifrar", "Por favor, ingrese la llave:")
        cifrado = cifrar(texto, llave, alphabet)
        print(cifrado)
        tk.Message(top, text=cifrado).pack()
        tk.Button(top, text="Copiar al portapapeles",
                  command=lambda: root.clipboard_append(cifrado)).pack()
    if opcion == "descifrar":
        # Crear una nueva ventana para ingresar datos necesarios segun cifrado
        texto = simpledialog.askstring(
            "Descifrar", "Por favor, ingrese el texto a descifrar:")
        llave = simpledialog.askinteger(
            "Descifrar", "Por favor, ingrese la llave:")
        descifrado = descifrar(texto, llave, alphabet)
        print(descifrado)
        tk.Message(top, text=descifrado).pack()
        tk.Button(top, text="Copiar al portapapeles",
                  command=lambda: root.clipboard_append(descifrado)).pack()


class cifradoUI(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Cifrado")
        self.pack(fill=tk.BOTH, expand=1)
        self.centerWindow()


def main_menu():
    global root
    root = tk.Tk()
    root.geometry("500x500+500+500")
    root.title("Criptografia")

    tk.Menu(root)

    tk.Label(root, text="Bienvenido a la aplicación de criptografía").pack()

    tk.Button(root, text="Cifrar",
              command=lambda: procesar_opcion("cifrar")).pack()

    tk.Button(root, text="Descifrar",
              command=lambda: procesar_opcion("descifrar")).pack()

    tk.Button(root, text="Cambiar alfabeto",
              command=lambda: cambiar_alfabeto).pack()

    root.mainloop()
