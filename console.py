
from alfabeto import cargar_alfabeto, cambiar_alfabeto
from cifrado_cesar import cifrar, descifrar


def config():
    global alphabet
    alphabet = cargar_alfabeto()
    if alphabet is None:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def console_menu():
    global alphabet
    config()
    print("Bienvenido a la aplicación de criptografía")

    def print_menu():
        print("Por favor, seleccione una opción:")
        print("1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Cambiar alfabeto")
        print("4. Salir")

    opcion = None
    while opcion != 4:
        print_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            texto = input("Por favor, ingrese el texto a cifrar: ")
            llave = int(input("Por favor, ingrese la llave: "))
            cifrado = cifrar(texto, llave, alphabet)
            print("Tu resultado es: \n" + cifrado)
            input("Presiona Enter para continuar...")
        elif opcion == "2":
            texto = input("Por favor, ingrese el texto a descifrar: ")
            llave = int(input("Por favor, ingrese la llave: "))
            descifrado = descifrar(texto, llave, alphabet)
            print("Tu resultado es: \n" + descifrado)
            input("Presiona Enter para continuar...")
        elif opcion == "3":
            alphabet = cambiar_alfabeto()
        elif opcion == "4":
            print("Gracias por usar la aplicación.")
            break
        elif opcion == "5":
            print(alphabet)
        else:
            print("Opción no válida.")
        opcion = None
