import string
from collections import Counter

spanish_freq = "eaosrnildctpumbfvqghjñkwxyz"
frecuencia_ingles = "etaoinshrdlcumwfgypbvkjxqz"


class CifradoMonoalfabetico:

    def __init__(self, alfabeto: list[str], console_mode=False):
        self.alfabeto = ''.join(alfabeto)
        self.dict = {}

    def console_config(self):
        pass

    def cifrar(self, texto: str):
        texto = texto.lower()
        opcion = input("¿Decimación (d) o aditivo (a)?: ").strip().lower()
        if opcion == 'd':
            key = int(input("Ingrese la clave: "))
            return self.decimacion(texto, key)

        elif opcion == 'a':
            key = int(input("Ingrese la clave: "))
            return self.desplazamiento(texto, key)

    def descifrar(self, texto: str):
        texto = texto.lower()
        opcion = input("¿Decimación (d) o aditivo (a)?: ").strip().lower()
        if opcion == 'd':
            key = int(input("Ingrese la clave: "))
            return self.desencriptar_decimacion(texto, key)

        elif opcion == 'a':
            key = int(input("Ingrese la clave: "))
            return self.desencriptar_desplazamiento(texto, key)

    def decimacion(self, text, key):
        texto_encriptado = "".join(self.alfabeto[(self.alfabeto.index(
            char) * key) % len(self.alfabeto)] if char in self.alfabeto else char for char in text.lower())
        return texto_encriptado

    def desplazamiento(self, text, key):
        for char in self.alfabeto:
            print(f"{char}: {self.alfabeto.index(char)}")
        texto_encriptado = "".join(self.alfabeto[(self.alfabeto.index(
            char) + key) % len(self.alfabeto)] if char in self.alfabeto else char for char in text.lower())
        return texto_encriptado

    def desencriptar_decimacion(self, text, key):
        # Calcula el inverso modular de la clave en mod len(alfabeto)
        inverse_key = pow(key, -1, len(self.alfabeto))
        decrypted_text = "".join(self.alfabeto[(self.alfabeto.index(
            char) * inverse_key) % len(self.alfabeto)] if char in self.alfabeto else char for char in text.lower())
        return decrypted_text

    def desencriptar_desplazamiento(self, text, key):

        decrypted_text = "".join(self.alfabeto[(self.alfabeto.index(
            char) - key) % len(self.alfabeto)] if char in self.alfabeto else char for char in text.lower())
        return decrypted_text


# # Solicitamos el método de cifrado
# method = input(
#     "Elige el método de cifrado: multiplicativo (m) o aditivo (a): ").strip().lower()
# key = int(input("Ingrese la clave: "))

# # Mensaje a encriptar
# message = "EL LOBO PARTIO CORRIENDO A TODA VELOCIDAD POR EL CAMINO QUE ERA MAS CORTO Y LA NIÑA SE FUE POR EL MAS LARGO ENTRETENIENDOSE EN COGER AVELLANAS EN CORRER TRAS LAS MARIPOSAS Y EN HACER RAMOS CON LAS FLORECILLAS QUE ENCONTRABA POCO TARDO EL LOBO EN LLEGAR A CASA DE LA ABUELA GOLPEA TOC TOC"
# if method == 'm':
#     ciphertext = encrypt_multiplicative(message, key)
# elif method == 'a':
#     ciphertext = desplazamiento(message, key)
# else:
#     raise ValueError("Método no válido")

# print("Texto encriptado:", ciphertext)

# # Intentamos descifrar
# if method == 'm':
#     decrypted_text = desencriptar_decimacion(ciphertext, key)
# elif method == 'a':
#     decrypted_text = desencriptar_desplazamiento(ciphertext, key)

# print("Texto desencriptado:", decrypted_text)
