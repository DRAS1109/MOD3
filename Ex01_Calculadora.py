#Calculadora com Funções
import math

def Soma(X, Y):
    """Função para somar X e Y e apresentar o resultado"""
    print (f"{X} + {Y} = {X + Y}")

def Subtração(X, Y):
    """Função para subtrair X e Y e apresentar o resultado"""
    print (f"{X} - {Y} = {X - Y}")

def Multiplicação(X, Y):
    """Função para multiplicar X e Y e apresentar o resultado"""
    print (f"{X} * {Y} = {round ((X * Y), 3)}")

def Divisão(X, Y):
    """Função para dividir X e Y e apresentar o resultado"""
    print (f"{X} / {Y} = {round ((X / Y), 3)}")


def Menu():
    """
    Mostra ao utilizador as operações que a calcuadora vai utilizar
    """

    Ação = None
    while Ação.upper().strip() != "T":

        Ação = input("Qual função pretende efetuar? \n + = Soma \n - = Subtração\n * = Multiplicação \n / = Divisão \n T = Terminar \n")
        if Ação == "5":
            break

        X = float(input(f"Introduza o 1º Nº: "))
        Y = float(input(f"Introduza o 2º Nº: "))

        if Ação.strip() == "+":
            #Ação_Extenso = "Somar"
            Soma(X, Y)

        elif Ação.strip() == "-":
            #Ação_Extenso = "Subtrair"
            Subtração(X, Y)

        elif Ação.strip() == "*":
            #Ação_Extenso = "Multiplicar"
            Multiplicação(X, Y)

        elif Ação.strip() == "/":
            #Ação_Extenso = "Dividir"
            Divisão(X, Y)


def main():
    Menu()

if __name__ == "__main__":
    main()