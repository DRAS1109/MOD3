"""
Menu: 1-Entrada\n 2-Saída\n 3-Estado\n 4-Terminar
N_Mesas N_clientes
Entrada: Quantos clientes e mesas que vão ocupar
Saida: Quantos clientes e mesas que vão desocupar e o preço da refeição
Estado: Mesas livres e ocupadas, clientes no restaurante e % de ocupação, custo de todas as refeiçoes de clientes que ja sairam
"""

import Utils

def Entrada_Clientes(Max_Lugares, N_Lugares_Ocupados):
    """
    Responsavel por ler quandos clientes entraram
    """
    if Max_Lugares == N_Lugares_Ocupados:
        print ("O restaurante está cheio")
        return 0

    #Nº de clientes que entraram
    Lugares_Livres = Max_Lugares - N_Lugares_Ocupados
    N_Clientes_E = Utils.Ler_Inteiro_Limites(1, Lugares_Livres, "Quantos clientes entraram? ")
    return N_Clientes_E

def Entrada_Mesas(Max_Mesas, N_Mesas_Ocupadas):
    """
    Responsavel por ler as mesas que vão ocupar
    """

    if Max_Mesas == N_Mesas_Ocupadas:
        return 0

    #Nº de mesas ocupadas
    Mesas_Livres = Max_Mesas - N_Mesas_Ocupadas
    N_Mesas_Ocupadas = Utils.Ler_Inteiro_Limites(1, Mesas_Livres, "Quantas mesas ocuparam? ")
    return N_Mesas_Ocupadas

def Saída_Clientes(N_Lugares_Ocupados):
    """
    Responsavel por registar a saida dos clientes
    """
    if N_Lugares_Ocupados == 0:
        print("Não tem clientes")
        return 0

    N_Clientes_S = Utils.Ler_Inteiro_Limites(1, N_Lugares_Ocupados, "Quantos clientes saíram? ")
    N_Lugares_Ocupados -= N_Clientes_S
    return N_Lugares_Ocupados

def Saída_Mesas(N_Mesas_Ocupadas):
    """
    Responsavel por ler as mesas que se vão liberar
    """
    if N_Mesas_Ocupadas == 0:
        print("Não tem mesas ocupadas")
        return 0
        
    N_Mesas_Desocupadas = Utils.Ler_Inteiro_Limites(1, N_Mesas_Ocupadas, "Quantas mesas desocuparam? ")
    N_Mesas_Ocupadas -= N_Mesas_Desocupadas
    return N_Mesas_Ocupadas

def Saída_Ref(Preço_Ref_Tot):
    """
    Responsavel por apresentar o preço de todas as refeições vendidas
    """
    Preço_Ref = Utils.Ler_Decimal_Limites(1, None, "Qual o preço da refeição? ")
    Preço_Ref_Tot += Preço_Ref
    return Preço_Ref_Tot

def Estado(Max_Lugares, N_Lugares_Ocupados, Max_Mesas, N_Mesas_Ocupadas, Preço_Ref_Tot):
    """
    Responsavel calcular e mostrar dados estatisticos do restaurante como:
    Mesas livres e ocupadas, clientes no restaurante e % de ocupação, custo de todas as refeiçoes já servidas
    """

    #Mesas e lugares livres
    Lugares_Livres = Max_Lugares - N_Lugares_Ocupados
    Mesas_Livres = Max_Mesas - N_Mesas_Ocupadas

    print(f"Tem {Lugares_Livres} lugares livres")
    print(f"Tem {Mesas_Livres} mesas livres")

    #Nº de clientes = N_Lugares_Atual
    print(f"Estão {N_Lugares_Ocupados} clientes no restaurante")

    #% de ocupação
    Ocupação = (N_Lugares_Ocupados / Max_Lugares) * 100
    print(f"Que corresponde a {Ocupação}% de ocupação")

    #Custo de todas as refeições = Preço_Ref_Tot
    print(f"De todos clientes que já saíram acumulou {Preço_Ref_Tot}€")

def Menu():
    """
    Responsavel por ler quantas mesas e lugares totais o restaurante tem e dar as opções do programa au utilizador
    """
    #N mesas e lugares totais
    Max_Lugares = Utils.Ler_Inteiro("Qual o Nº de clientes que o restaurante pode receber? ")
    Max_Mesas = Utils.Ler_Inteiro("Qual o Nº de mesas do restaurante? ")

    #N mesas e clientes atualmente no restaurante
    N_Lugares_Ocupados = 0
    N_Mesas_Ocupadas = 0
    Preço_Ref_Tot = 0

    X = 1
    while X != 4:
        X = Utils.Ler_Inteiro_Limites(1, 4, "Qual operação pretende efetuar: \n 1-Entrada \n 2-Saída \n 3-Estado \n 4-Terminar \n ")
        if X == 1:
            N_Clientes_E = Entrada_Clientes(Max_Lugares, N_Lugares_Ocupados)
            N_Lugares_Ocupados += N_Clientes_E

            N_Mesas_E = Entrada_Mesas(Max_Mesas, N_Mesas_Ocupadas)
            N_Mesas_Ocupadas += N_Mesas_E

        elif X == 2:
            Saída_Clientes(N_Lugares_Ocupados)
            Saída_Mesas(N_Mesas_Ocupadas)
            Preço_Ref_Tot = Saída_Ref(Preço_Ref_Tot)
        elif X == 3:
            Estado(Max_Lugares, N_Lugares_Ocupados, Max_Mesas, N_Mesas_Ocupadas, Preço_Ref_Tot)
    

def main():
    Menu()

if __name__ == "__main__":
    main()