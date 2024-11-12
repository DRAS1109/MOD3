def Menu():
    """
    Mostra ao utilizados as operações que a calcuadora vai utilizar
    """
    Ação = input("Qual função pretende efetuar? \n + = Soma \n - = Subtração\n * = Multiplicação \n / = Divisão")
    if Ação == "+":
        Soma()

    elif Ação == "-":
        Subtração()

    elif Ação == "*":
        Multiplicação()

    elif Ação == "/":
        Divisão()

        
def main():
    Menu()



if __name__ == "__main__":
    main()