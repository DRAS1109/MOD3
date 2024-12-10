import Utils
import math

def Lucro():
    Lucro = Utils.Ler_Decimal_Limites(0, None, "Quanto é que lucraram com este saque? ")
    return Lucro

def Divisão_Chefe(Lucro):
    # Chefe = 50%
    Chefe = Lucro * 0.5
    Chefe = round(Chefe, 2)
    return Chefe

def Divisão_Musculos(Lucro):
    # Musculos (2) ==
    Musculos = Lucro * 0.2
    Musculos = round(Musculos, 2)
    return Musculos

def Divisão_Condutor(Lucro):
    # Condutor = Musculos / 2
    Condutor = Lucro * 0.1
    Condutor = round(Condutor, 2)
    return Condutor

def Apresentação(Chefe, Musculos, Condutor):
    print(f"Com esque saque o chefe ganhou {Chefe}€")
    print(f"O Musculos 1 ganhou {Musculos} e o Musculo 2 ganhou {Musculos}€")
    print(f"O condutor ganhou {Condutor}€")

def Gastar(Dinheiro):
        Sobra = Dinheiro * 0.5
        Meses = 0

        #Quantos meses dura o dinheiro
        Plano = Sobra * 0.05
        if Plano > 1000:
            Plano = 1000

        while True:
            Sobra = Sobra - Plano
            if Sobra < 0:
                break
            Meses = Meses + 1
        
        print(f"Os {Dinheiro}€ podem ser gastos em {Meses} Meses, gastando {Plano}€ por mes")

        #Quanto se terá ao fim de 10 anos
        Reforma = (Dinheiro * 0.5) * ((1.05)**10)
        print (f"Ao fim de 10 anos terá {round(Reforma, 2)}€")

def main():
    # Função principal do programa
    Lucro_D = Lucro()

    Chefe = Divisão_Chefe(Lucro_D)
    Musculos = Divisão_Musculos(Lucro_D)
    Condutor = Divisão_Condutor(Lucro_D)

    Apresentação(Chefe, Musculos, Condutor)

    Qual = Utils.Ler_Inteiro_Limites (1, 3, "Quem é que quer gastar o dinheiro? \n 1 - Chefe \n 2 - Musculos \n 3 - Condutor \n ")
    if Qual == 1:
        Dinheiro = Chefe
    elif Qual == 2:
        Dinheiro = Musculos
    elif Qual == 3:
        Dinheiro = Condutor

    Gastar(Dinheiro)

if __name__=="__main__":
    main()