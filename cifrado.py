from abc import ABC, abstractmethod


class cifrado(ABC):
    self.nombre = ""

    def __init__(self, alfabeto, nombre):
        self.alfabeto = alfabeto
        self.nombre = nombre

    def config(self, **kwargs):
        pass

    @abstractmethod
    def cifrar(self, texto: str):
        pass

    @abstractmethod
    def descifrar(self, texto: str):
        pass
