import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# Crear una ventana oculta
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

# key = int(input("Por favor, ingrese la llave: "))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cambiar_alfabeto():
    new_alphabet = []
    # Abrir el cuadro de diálogo para seleccionar un archivo
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt")]
    )

    # Verificar si se seleccionó un archivo
    if file_path:
        try:
            # Abrir el archivo y leer línea por línea
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    # print(line.strip())  # Imprimir la línea sin saltos de línea extra
                    new_alphabet.append(line.strip())
            alphabet = new_alphabet
            return new_alphabet
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    else:
        print("No se seleccionó ningún archivo.")

# if input("Quiere seleccionar su propio? [y] si ") == 'y':
#     cambiar_alfabeto()


# texto_plano = str(input("Por favor, ingrese el texto a cifrar: "))


def procesar_opcion(opcion):
    # Crear una nueva ventana para ingresar la llave y el texto
    ventana_entrada = tk.Toplevel()
    ventana_entrada.title(f"{opcion.capitalize()} Texto")

    # Etiquetas y campos de entrada para la llave y el texto
    tk.Label(ventana_entrada, text="Ingresa la llave (número):").pack()
    llave_entrada = tk.Entry(ventana_entrada)
    llave_entrada.pack()

    tk.Label(ventana_entrada, text="Ingresa el texto:").pack()
    texto_entrada = tk.Entry(ventana_entrada)
    texto_entrada.pack()

    # Función que se ejecuta al hacer clic en el botón
    def ejecutar():
        try:
            llave = int(llave_entrada.get())  # Convertir la llave a entero
            texto = texto_entrada.get()

            if opcion == "cifrar":
                resultado = cifrar(texto, llave)
                messagebox.showinfo("Resultado", f"Texto cifrado: {resultado}")
            elif opcion == "descifrar":
                resultado = descifrar(texto, llave)
                messagebox.showinfo(
                    "Resultado", f"Texto descifrado: {resultado}")
        except ValueError:
            messagebox.showerror(
                "Error", "La llave debe ser un número entero.")

    # Botón para ejecutar el cifrado/descifrado
    tk.Button(ventana_entrada, text="Ejecutar", command=ejecutar).pack()


def menu_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú de Cifrado y Descifrado")

    # Función para mostrar las opciones
    def mostrar_opciones():
        opcion = simpledialog.askstring(
            "Opciones", "Selecciona una opción:\n1. Cifrar\n2. Descifrar\n3. Cambiar alfabeto")

        if opcion == "1":
            procesar_opcion("cifrar")
        elif opcion == "2":
            procesar_opcion("descifrar")
        elif opcion == "3":
            alphabet = cambiar_alfabeto()
        else:
            messagebox.showerror("Error", "Opción no válida.")

    # Botón para mostrar las opciones
    tk.Button(ventana_principal, text="Mostrar Opciones",
              command=mostrar_opciones).pack()

    # Ejecutar la ventana principal
    ventana_principal.mainloop()


menu_principal()
