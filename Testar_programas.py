import Utils

"""
X = Utils.Ler_Inteiro()
print (X)

X = Utils.Ler_Inteiro("Introduza um valor: ")
print (X)
"""

"""
X = Utils.Ler_Inteiro_Limites(2, 10)
print (X)

X = Utils.Ler_Inteiro_Limites(2,10,"Introduza um valor: ")
print (X)

X = Utils.Ler_Inteiro_Limites(2, None)
print (X)

X = Utils.Ler_Inteiro_Limites(2)
print (X)
"""

"""
X = Utils.Ler_Decimal("Introduza um numero: ")
print (X)
"""

"""
X = Utils.Ler_Decimal_Limites(2, 10)
print (X)

X = Utils.Ler_Decimal_Limites(2,10.5,"Introduza um valor: ")
print (X)

X = Utils.Ler_Decimal_Limites(2.5, None)
print (X)

X = Utils.Ler_Decimal_Limites(2.5)
print (X)
"""


Frase = input("Introduza uma frase: ")
Frase = Frase.lower()

for X in range (97, 122 + 1):
    Contar = 0
    for i in Frase:
        if ord(i) == X:
            Contar += 1
    if Contar > 0:
        print (f"A função tem {Contar} letras {chr(X)}")