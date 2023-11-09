from dado1 import Dado

def programa_de_prueba():
    dado1 = Dado()
    dado2 = Dado()
    
    for _ in range(5):
        dado1.lanzar()
        dado2.lanzar()
        print(f"Dado 1: {dado1.numero}, Dado 2: {dado2.numero}")

if __name__ == "__main__":
    programa_de_prueba()
