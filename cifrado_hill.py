import numpy as np
from sympy import Matrix
import tkinter as tk
from tkinter import ttk


class CifradoHill:
    nombre = "Cifrado Hill"

    def __init__(self, alfabeto: list[str], console_mode=False):
        # self.matriz_llave = matriz_llave
        self.alfabeto = alfabeto
        # with_ui = input(
        #     "¿Desea configurar la matriz clave de Hill con una interfaz gráfica? (s/n): ").lower() == 's'
        # self.config(with_ui)
        console_mode if self.console_config() else self.ui_config()
        # self.dimension = matriz_llave.shape[0]
        # self.inversa_llave = np.array(Matrix(
        #     self.matriz_llave).inv_mod(len(alfabeto)))

    def console_config(self, with_ui: bool = False):
        def define_matrix(in_matriz):
            self.matriz_llave = np.array(eval(in_matriz))
            # self.matriz_llave = Matrix.T
            print("Matriz ingresada:", self.matriz_llave)
            self.dimension = self.matriz_llave.shape[0]
            print("Dimensión de la matriz:", self.dimension)
            if np.gcd(Matrix(self.matriz_llave).det(), len(self.alfabeto)) != 1:
                raise ValueError(
                    "El determinante de la matriz debe ser coprimo con la longitud del alfabeto.")
            self.inversa_llave = np.array(Matrix(
                self.matriz_llave).inv_mod(len(self.alfabeto)))

        if with_ui:
            root = tk.Tk()
            root.title("Matriz Clave Hill")

            frame = HillCipherKeyMatrix(root)
            frame.pack(padx=10, pady=10)

            def show_matrix():
                try:
                    in_matriz = str(frame.get_matrix())
                    print(in_matriz)
                    print(type(in_matriz))
                    define_matrix(in_matriz)
                except ValueError as e:
                    print(e)
                    return
                root.destroy()

            btn = ttk.Button(root, text="Obtener Matriz", command=show_matrix)
            btn.pack(pady=5)

            root.mainloop()
        else:
            print("Configuración de matriz clave Hill")
            print("Ingrese la matriz clave de Hill")
            print("Ejemplo de matriz 2x2: [[1, 2], [3, 4]]")
            print("Ejemplo de matriz 3x3: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
            is_valid = False
            while not is_valid:
                try:
                    in_matriz = input("Matriz: ")
                    define_matrix(in_matriz)
                    is_valid = True

                except ValueError as e:
                    print(e)
                    continue

    def ui_config(self):
        pass

    def _texto_a_numeros(self, texto: str) -> list[int]:
        return [self.alfabeto.index(letra) for letra in texto]

    def _numeros_a_texto(self, numeros: list[int]) -> str:
        return ''.join(self.alfabeto[numero] for numero in numeros)

    def matriz_a_encriptar(self, lista: list) -> np.ndarray:
        if all(isinstance(i, str) for i in lista):
            lista_numeros = self._texto_a_numeros(''.join(lista))
        elif all(isinstance(i, int) for i in lista):
            lista_numeros = lista
        else:
            raise ValueError(
                "La lista debe contener solo enteros o solo cadenas de texto.")

        return np.array([lista_numeros[i:i+self.dimension] for i in range(0, len(lista_numeros), self.dimension)])

    def cifrar(self, texto: str) -> str:
        mod = len(self.alfabeto)
        n = self.dimension

        texto = self.validar_y_normalizar_texto(texto)
        texto_numeros = self._texto_a_numeros(texto)

        # matriz_a_encriptar = self.matriz_a_encriptar(texto_numeros)
        # print("Matriz: ", matriz_a_encriptar)
        texto_cifrado_numeros: list[int] = []
        for i in range(0, len(texto_numeros), n):
            block = np.array(texto_numeros[i:i+n]).reshape(-1, 1)
            encrypted_block = (self.matriz_llave @ block) % mod
            texto_cifrado_numeros.extend(encrypted_block.flatten())

        # for i in range(matriz_a_encriptar.shape[0]):
        #     texto_cifrado_numeros.extend(
        #         np.dot(self.matriz_llave, matriz_a_encriptar[i]) % len(self.alfabeto))
        #     print("Multiplicación: ", matriz_a_encriptar[i], np.dot(
        #         self.matriz_llave, matriz_a_encriptar[i]))

        return self._numeros_a_texto(texto_cifrado_numeros)

    def validar_y_normalizar_texto(self, texto: str) -> str:

        # Se convierte el texto a mayúsculas y se eliminan los espacios
        texto = texto.replace(' ', '')
        # Si el texto no es múltiplo de la dimensión de la matriz, se rellena con 'X'
        if len(texto) % self.dimension != 0:
            texto += 'x' * (self.dimension - len(texto) % self.dimension)
        return texto

    def descifrar(self, texto_cifrado: str) -> str:
        texto_cifrado_numeros = self._texto_a_numeros(texto_cifrado)
        matriz_a_encriptar = self.matriz_a_encriptar(texto_cifrado_numeros)
        # print("Matriz: ", matriz_a_encriptar)
        texto_descifrado_numeros: list[int] = []
        for i in range(matriz_a_encriptar.shape[0]):
            texto_descifrado_numeros.extend(
                np.dot(self.inversa_llave, matriz_a_encriptar[i]) % len(self.alfabeto))
        return self._numeros_a_texto(texto_descifrado_numeros)


class HillCipherKeyMatrix(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid_size = tk.IntVar(value=2)
        self.entries = []

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Tamaño de matriz:").grid(
            row=0, column=0, padx=5, pady=5)

        size_selector = ttk.Combobox(self, textvariable=self.grid_size, values=[
                                     2, 3], state="readonly")
        size_selector.grid(row=0, column=1, padx=5, pady=5)
        size_selector.bind("<<ComboboxSelected>>", self.update_matrix)

        self.matrix_frame = tk.Frame(self)
        self.matrix_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.update_matrix()

    def validate_input(self, P):
        return P.isdigit() or P == ""

    def update_matrix(self, event=None):
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

        self.entries = []
        size = self.grid_size.get()

        vcmd = (self.register(self.validate_input), "%P")

        for i in range(size):
            row_entries = []
            for j in range(size):
                entry = ttk.Entry(self.matrix_frame,
                                  width=5, justify='center', validate='key', validatecommand=vcmd)
                entry.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(entry)
            self.entries.append(row_entries)

    def get_matrix(self):
        try:
            return [[int(entry.get()) for entry in row] for row in self.entries]
        except ValueError:
            print("Error: Asegúrate de ingresar solo números.")
            return None


# # Prueba
# alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
#             'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# # matriz_llave = np.array([[1, 2, 3], [0, 4, 5], [1, 0, 6]])

# cifrado_hill = CifradoHill(alfabeto)

# texto = "CUADERNO DE CULTURA CIENTIFICA EE"

# texto_cifrado = cifrado_hill.cifrar(texto)

# print("Texto cifrado: ", texto_cifrado)

# texto_descifrado = cifrado_hill.descifrar(texto_cifrado)

# print("Texto descifrado: ", texto_descifrado)
