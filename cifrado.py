from abc import ABC, abstractmethod


class cifrado(ABC):
    def __init__(self, alfabeto):
        self.alfabeto = alfabeto

    def config(self, **kwargs):
        pass

    @abstractmethod
    def cifrar(self, texto: str):
        pass

    @abstractmethod
    def descifrar(self, texto: str):
        pass
