import math

class Punto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def invertir_coordenadas(self):
        self.__x, self.__y = self.__y, self.__x

    def distancia(self, other_point):
        return math.sqrt((self.__x - other_point.x)**2 + (self.__y - other_point.y)**2)

    def __str__(self):
        return f"({self.__x}, {self.__y})"
