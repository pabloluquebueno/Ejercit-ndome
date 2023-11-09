from punto import Punto


def programa_de_prueba():
    punto = Punto(3, 4)

    print("Punto inicial:", punto)

    print("Coordenada x:", punto.x)

    punto.x = 0

    print("Punto después de cambiar la coordenada x:", punto)

if __name__ == "__main__":
    programa_de_prueba()
