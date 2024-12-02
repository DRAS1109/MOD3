"""
Programa para calcular todos os quadrados dos numeros ate N
"""

import Ex10_Quadrado
import math

def Soma_Quadrados(N):
    Quadrados = 0
    for i in range (1, N + 1):
        Quadrados = Quadrados + Ex10_Quadrado.Calcular_Quadrado(i)

    return Quadrados

def main():
    assert Soma_Quadrados(3) == 14, "A Função deveria devolver 14"
    assert Soma_Quadrados(5) == 55, "A Função deveria devolver 55"
    print ("A função passou nos testes")

if __name__ == "__main__":
    main()