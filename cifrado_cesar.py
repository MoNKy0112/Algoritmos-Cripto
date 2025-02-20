import string


class CifradoCesar:
    nombre = "Cifrado Cesar"

    def __init__(self, alfabeto, console_mode=False):
        self.alfabeto = alfabeto
        console_mode if self.console_config() else self.ui_config()

    def console_config(self):
        self.key = int(input("Ingrese la clave: "))
        pass

    def ui_config(self):
        pass

    def cifrar(self, texto_plano):
        texto_plano = texto_plano.replace(" ", "")
        final_word = ""
        for letter in texto_plano:
            try:
                new_index = (self.alfabeto.index(
                    letter) + self.key) % len(self.alfabeto)

                final_word += self.alfabeto[new_index]
                # print(alfabeto[new_index])
            except Exception as e:
                print("Error")
                print(e)
        return final_word

    def descifrar(self, texto_cifrado):
        final_word = ""
        for letter in texto_cifrado:
            try:
                new_index = (self.alfabeto.index(
                    letter) - self.key) % len(self.alfabeto)

                final_word += self.alfabeto[new_index]
                # print(alfabeto[new_index])
            except Exception as e:
                print("Error")
                print(e)
        return final_word

# Pureba


# alfabeto = list(string.ascii_uppercase)
# cifrado = CifradoCesar(alfabeto, 3)
# texto = "HOLA MUNDO".replace(" ", "")
# texto_cifrado = cifrado.cifrar(texto)
# print(texto_cifrado)
# texto_descifrado = cifrado.descifrar(texto_cifrado)
# print(texto_descifrado)
