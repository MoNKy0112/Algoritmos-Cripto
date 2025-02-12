import numpy as np
from sympy import Matrix


class CifradoHill:
    def __init__(self, matriz_llave: np.ndarray, alfabeto: list[str]):
        self.matriz_llave = matriz_llave
        self.alfabeto = alfabeto
        self.dimension = matriz_llave.shape[0]
        self.inversa_llave = np.array(Matrix(
            self.matriz_llave).inv_mod(len(alfabeto)))

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
        texto = self.validar_y_normalizar_texto(texto)
        texto_numeros = self._texto_a_numeros(texto)
        matriz_a_encriptar = self.matriz_a_encriptar(texto_numeros)
        texto_cifrado_numeros: list[int] = []
        for i in range(matriz_a_encriptar.shape[0]):
            texto_cifrado_numeros.extend(
                np.dot(self.matriz_llave, matriz_a_encriptar[i]) % len(self.alfabeto))
        return self._numeros_a_texto(texto_cifrado_numeros)

    def validar_y_normalizar_texto(self, texto: str) -> str:

        # Se convierte el texto a mayúsculas y se eliminan los espacios
        texto = texto.upper().replace(' ', '')
        # Si el texto no es múltiplo de la dimensión de la matriz, se rellena con 'X'
        if len(texto) % self.dimension != 0:
            texto += 'X' * (self.dimension - len(texto) % self.dimension)
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


alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
matriz_llave = np.array([[1, 2, 3], [0, 4, 5], [1, 0, 6]])

cifrado_hill = CifradoHill(matriz_llave, alfabeto)

texto = "CUADERNO DE CULTURA CIENTIFICA EE"

texto_cifrado = cifrado_hill.cifrar(texto)

print("Texto cifrado: ", texto_cifrado)

texto_descifrado = cifrado_hill.descifrar(texto_cifrado)

print("Texto descifrado: ", texto_descifrado)
