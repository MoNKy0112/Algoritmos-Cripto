import random
import string


class CifradoMonoalfabetico:
    nombre = "Cifrado Monoalfabetico"

    def __init__(self, alfabeto: list[str], console_mode=False):
        self.alfabeto = alfabeto
        self.dict = {}
        self.crear_dict()
        console_mode if self.console_config() else self.ui_config()
        pass

    def console_config(self):
        clave = input(
            "Ingrese la clave: \n Ejemplo de clave: E,T,U,O,A,D,S,N,I,R,L,C,P,M,B,Q,G,H,F,J,K,V,W,X,Y,Z\n")
        self.clave = clave.split(",")
        pass

    def ui_config(self):
        pass

    def crear_dict(self):
        self.dict = dict(zip(self.alfabeto, self.clave))

    def cifrar(self, texto: str):
        texto = texto.upper().replace(" ", "")
        texto_cifrado = ""
        for letra in texto:
            texto_cifrado += self.dict[letra]
        return texto_cifrado

    def descifrar(self, texto: str):
        texto = texto.upper().replace(" ", "")
        texto_descifrado = ""
        for letra in texto:
            for key, value in self.dict.items():
                if value == letra:
                    texto_descifrado += key
                    break
        return texto_descifrado


# # Prueba
# alfabeto = list(string.ascii_uppercase)
# clave = alfabeto[:]
# random.shuffle(clave)
# cifrado = cifrado_monoalfabetico(alfabeto, clave)
# texto = "HOLA MUNDO"
# texto_cifrado = cifrado.cifrar(texto)
# print(texto_cifrado)
# texto_descifrado = cifrado.descifrar(texto_cifrado)
# print(texto_descifrado)
