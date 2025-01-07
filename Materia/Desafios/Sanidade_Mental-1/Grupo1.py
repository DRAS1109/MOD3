#Grupo 1
"""
Ex 1
Cria uma função que recebo dois parametros. 
A função deve calculare e mostrar a soma de todos os numeros inteiros entre os dois parametros.
"""
def Soma(N1: int, N2: int) -> int:
    Soma_Todos = 0
    for x in range (N1, N2 + 1):
        Soma_Todos = Soma_Todos + x
    print (f"A soma de todos os Nº entre {N1} e {N2} inclusive é: {Soma_Todos}")


"""
Ex 2
Cria uma função que calcula a média de 5 valores.
A função deve ler os valores do utilizador, calcular e mostrar a média dos valores
"""
def Media1():
    N1 = float(input("Introduza uma Nota "))
    N2 = float(input("Introduza uma Nota "))
    N3 = float(input("Introduza uma Nota "))
    N4 = float(input("Introduza uma Nota "))
    N5 = float(input("Introduza uma Nota "))

    Media = (N1 + N2 + N3 + N4 + N5) / 5

def Media2():
    Soma = 0
    for _ in range (5):
        Nota = float(input("Introduza uma Nota "))
        Soma = Soma + Nota

    Media = Soma / 5
    print (f"A media é: {Media}")