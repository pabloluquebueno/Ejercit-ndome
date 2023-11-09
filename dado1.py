import random

class Dado:
    def __init__(self, caras=6):
        self.__caras = caras
        self.__numero = random.randint(1, self.__caras)

    @property
    def numero(self):
        return self.__numero

    @property
    def caras(self):
        return self.__caras

    @caras.setter
    def caras(self, valor):
        self.__caras = valor

    def __repr__(self):
        return f"El número es {self.__numero} y el número de caras del dado es: {self.__caras}"

    def lanzar(self):
        self.__numero = random.randint(1, self.__caras)