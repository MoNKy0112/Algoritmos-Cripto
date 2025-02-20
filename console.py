
from alfabeto import cargar_alfabeto, cambiar_alfabeto
from texto import cargar_texto, cambiar_texto
from cifrado_cesar import CifradoCesar
from cifrado_monoalfabetico import CifradoMonoalfabetico
from cifrado_playfair import CifradoPlayfair
from cifrado_hill import CifradoHill

global alfabeto, cifrado_actual, texto_actual
cifrado_actual = None
texto_actual = ""
cifrados = [CifradoCesar, CifradoMonoalfabetico, CifradoPlayfair, CifradoHill]


def config():
    global alfabeto, cifrado_actual, texto_actual
    alfabeto = cargar_alfabeto()
    if alfabeto is None:
        alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    texto_actual = cargar_texto(alfabeto)
    if texto_actual is None:
        texto_actual = ""
    select_cifrado()


def select_cifrado():
    global cifrado_actual

    def select_cifrado_menu():
        print("Por favor, seleccione un cifrado:")
        print("1. Cifrado Cesar")
        print("2. Cifrado Monoalfabetico")
        print("3. Cifrado Playfair")
        print("4. Cifrado Hill")
        # print("5. Cifrado Vigenere")
        # print("6. Cifrado RSA")
        # print("7. Cifrado ElGamal")
        # print("8. Cifrado Diffie-Hellman")

    while cifrado_actual not in cifrados:
        select_cifrado_menu()
        opcion = input("Opción: ")
        if opcion == "1":
            cifrado_actual = CifradoCesar(alfabeto, True)
        elif opcion == "2":
            cifrado_actual = CifradoMonoalfabetico(alfabeto, True)
        elif opcion == "3":
            cifrado_actual = CifradoPlayfair(alfabeto, True)
        elif opcion == "4":
            cifrado_actual = CifradoHill(alfabeto, True)
        else:
            print("Opción no válida.")


def add_text():
    global texto_actual
    opcion = None
    while opcion not in ["1", "2"]:
        print("por favor ingrese un texto a cifrar/descifrar")
        print("Seleccione el metodo para ingresar el texto:\n1. Ingresar texto por consola\n2. Ingresar texto por archivo")
        opcion = input("Opción: ")
        if opcion == "1":
            texto_actual = input("Por favor, ingrese el texto a cifrar: ")
        elif opcion == "2":
            texto_actual = input("Por favor, ingrese el texto a cifrar: ")
            texto_actual = cambiar_texto(alfabeto)
        else:
            print("Opción no válida.")


def console_menu():
    global alfabeto, cifrado_actual, texto_actual
    config()
    print("Bienvenido a la aplicación de criptografía")

    # def print_menu():
    #     print("Por favor, seleccione una opción:")
    #     print("1. Cifrar texto")
    #     print("2. Descifrar texto")
    #     print("3. Cambiar alfabeto")
    #     print("4. Mostrar alfabeto")
    #     print(f"5. Cambiar tipo de cifrado (Actual: ${cifrado_actual})")
    #     print("6. Salir")

    def print_menu():
        print("Por favor, seleccione una opción:")
        print("1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Cambiar alfabeto")
        print("4. Cambiar texto a cifrar/descifrar")
        print("5. Cambiar tipo de cifrado")
        print("6. Mostrar alfabeto")
        print("7. Mostrar texto a cifrar/descifrar")
        print("8. Salir")

    opcion = None
    flag_exit = False
    while not flag_exit:
        print_menu()
        opcion = input("Opción: ")
        if opcion == "1":
            if texto_actual == "":
                add_text()
            else:
                cifrado_actual.cifrar(texto_actual)
        if opcion == "2":
            if texto_actual == "":
                add_text()
            else:
                cifrado_actual.descifrar(texto_actual)
        if opcion == "3":
            alfabeto = cambiar_alfabeto()
        if opcion == "4":
            texto_actual = cambiar_texto(alfabeto)
        if opcion == "5":
            select_cifrado()
        if opcion == "6":
            print(alfabeto)
        if opcion == "7":
            print(texto_actual)
        if opcion == "8":
            flag_exit = True
        else:
            print("Opción no válida.")

    # opcion = None
    # while opcion != 4:
    #     print_menu()
    #     opcion = input("Opción: ")

    #     if opcion == "1":
    #         texto = input("Por favor, ingrese el texto a cifrar: ")
    #         llave = int(input("Por favor, ingrese la llave: "))
    #         cifrado = cifrar(texto, llave, alfabeto)
    #         print("Tu resultado es: \n" + cifrado)
    #         input("Presiona Enter para continuar...")
    #     elif opcion == "2":
    #         texto = input("Por favor, ingrese el texto a descifrar: ")
    #         llave = int(input("Por favor, ingrese la llave: "))
    #         descifrado = descifrar(texto, llave, alfabeto)
    #         print("Tu resultado es: \n" + descifrado)
    #         input("Presiona Enter para continuar...")
    #     elif opcion == "3":
    #         alfabeto = cambiar_alfabeto()
    #     elif opcion == "4":
    #         print(alfabeto)
    #     elif opcion == "5":
    #         break
    #     elif opcion == "6":
    #         print("Gracias por usar la aplicación.")
    #         break
    #     elif opcion == "5":
    #         print(alfabeto)
    #     else:
    #         print("Opción no válida.")
    #     opcion = None
