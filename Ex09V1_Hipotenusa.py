"""
Programna para calcular a hipotenusa a partir de 2 catetos fornecidos pelo utilizador
"""

import math

def Calcular_Hipotenusa(C1:float, C2:float) -> float:
    Hipotenusa = math.pow(C1,2) + math.pow(C2,2)
    Hipotenusa = math.sqrt(Hipotenusa)
    Hipotenusa = round(Hipotenusa, 3)
    return Hipotenusa

def main():
    assert Calcular_Hipotenusa(3, 4) == 5, "A Função deveria devolver 5"
    print ("A função passou nos testes")

if __name__ == "__main__":
    main()