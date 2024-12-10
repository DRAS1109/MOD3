"""
Programa para calcular o vencimento de um trabalhador.
O programa deve começar por solicitar ao trabalhador que indique o seu nome, quantas horas trabalhou por dia, 
e quanto ganha por hora. Caso o trabalho tenho mais do que 8 horas de trabalho deve receber, por cada hora 
extra recebe mais 25%. Caso tenho trabalho mais do que 10 horas por dia deve receber 50% por cada hora além 
das 10 horas.
"""
import Utils 
import sys

def PedirNomeTrabalhador():
    """
    Esta função deve pedir o nome do trabalhador. O nome deve ter pelo menos 3 letras.
    Caso ja tenha sido inserido no terminal não será pedido
    """

    nome = Utils.Ler_Nome_Litimes(3, None, "Introduza o seu nome: ")
    return nome

def PedirHorasTrabalho():
    """Esta função pede ao utilizador quantas horas trabalho no dia. O nº de horas deve ser superior a zero."""

    horas = Utils.Ler_Inteiro_Limites(0, None, "Quantas horas trabalhou? ")
    return horas

def PedirOrdenado():
    """Esta função pede ao utilizado quanto ganha por cada hora de trabalho"""

    ordenado_por_hora = Utils.Ler_Decimal_Limites(0, None, "Quanto ganha por hora? ")
    return ordenado_por_hora

def MostrarVencimento(nome,horas,ordenado_por_hora):
    """Esta função deve mostrar o nome do trabalhador e quanto é que deve receber pelo dia de trabalho"""
    if horas <= 8:
        ordenado = horas * ordenado_por_hora

    elif horas <= 10:
         ordenado = (8 * ordenado_por_hora) + ((horas - 8) * (ordenado_por_hora *1.25))
    
    else:
         ordenado = (8 * ordenado_por_hora) + (2 * (ordenado_por_hora * 1.25)) + ((horas - 10) * (ordenado_por_hora * 1.5))

    print (f"O {nome} deverá receber {ordenado}€")

def main():
    # Função principal do programa
    if len(sys.argv) > 1:
        nome = sys.argv[1]
    else:
        nome = PedirNomeTrabalhador()
    horas = PedirHorasTrabalho()
    ordenado_por_hora = PedirOrdenado()
    MostrarVencimento(nome,horas,ordenado_por_hora)

if __name__=="__main__":
    main()