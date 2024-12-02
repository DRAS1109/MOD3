"""
Programa para calcular o quadrado de um numero inteiro, n
"""

import math

def Calcular_Quadrado(N:int) -> int:
    Quadrado = math.pow(N,2)
    Quadrado = round(Quadrado)
    return Quadrado

def main():
    assert Calcular_Quadrado(4) == 16, "A Função deveria devolver 16"
    print ("A função passou nos testes")

if __name__ == "__main__":
    main()