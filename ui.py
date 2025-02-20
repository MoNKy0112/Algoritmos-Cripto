import tkinter as tk
from tkinter import Frame, filedialog, simpledialog, messagebox

from alfabeto import cargar_alfabeto, cambiar_alfabeto
import cifrado_cesar


def config():
    global alphabet
    alphabet = cargar_alfabeto()
    if alphabet is None:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class cifradoUI(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global resultLabel

        def only_numbers(char):
            return char.isdigit()
        validation = root.register(only_numbers)

        self.master.title("Cifrado")
        self.pack(fill=tk.BOTH, expand=1)

        lbl = tk.Label(self, text="Cifrado")
        lbl.grid(row=0, column=0, sticky=tk.W, pady=4, padx=5)

        text = tk.Text(self, height=20, width=50)
        text.grid(row=1, column=0, columnspan=2, rowspan=4,
                  pady=4, padx=5, sticky=tk.W+tk.E+tk.N+tk.S)

        key = tk.Spinbox(self, from_=0, increment=1,
                         textvariable=tk.IntVar(value=3), validate="key", validatecommand=(validation, '%S'))
        key.grid(row=1, column=2, pady=4, padx=5)

        resultLabel = tk.Label(self, text="Resultado = ")
        resultLabel.grid(row=5, column=0, columnspan=2,
                         pady=4, padx=5, sticky=tk.W)

        btn_cifrar = tk.Button(self, text="Cifrar",
                               command=lambda: self.cifrar_ui(text.get("1.0", "end-1c"), int(key.get())))
        btn_cifrar.grid(row=6, column=0, pady=4, padx=5, sticky=tk.W+tk.E)

        btn_descifrar = tk.Button(
            self, text="Descifrar", command=lambda: self.descifrar_ui(str(text.get("1.0", "end-1c")), int(key.get())))
        btn_descifrar.grid(row=6, column=1, pady=4, padx=5, sticky=tk.W+tk.E)

        btn_cambiar_alfabeto = tk.Button(
            self, text="Cambiar alfabeto", command=lambda: self.cambiar_alfabeto())
        btn_cambiar_alfabeto.grid(
            row=6, column=2, pady=4, padx=5, sticky=tk.W+tk.E)
        chk_space = tk.Checkbutton(
            self, text="Incluir espacios", variable=tk.BooleanVar())
        chk_space.grid(row=7, column=0, pady=4, padx=5, sticky=tk.W+tk.E)

    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro que deseas salir?"):
            self.master.destroy()

    def cambiar_alfabeto(self):
        global alphabet
        alphabet = cambiar_alfabeto()

    def cifrar_ui(self, texto, llave):
        global resultLabel

        result = cifrar(texto, llave, alphabet)
        print(result)
        resultLabel.config(text="Resultado = " + result)

    def descifrar_ui(self, texto, llave):
        global resultLabel

        result = descifrar(texto, llave, alphabet)
        resultLabel.config(text="Resultado = " + result)


def main_menu():
    global root, alphabet
    config()
    root = tk.Tk()
    root.geometry("600x600+500+300")
    app = cifradoUI()
    root.mainloop()
