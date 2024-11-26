#Estacionamento
import datetime

def Preço():
    Preço_Min = float(input("Qual é o preço por 15min no estacionamento? "))
    return Preço_Min


def Tempo():
    Entrada_H = int(input("Introduza as horas em que entrou no estacionamento (EX: 16): "))
    Entrada_M = int(input("Introduza os minutos em que entrou no estacionamento (EX: 35): "))

    if Entrada_H >= 0 and Entrada_H <= 23 and Entrada_M >= 0 and Entrada_M <= 60:
        Saida_H = datetime.datetime.now().hour
        Saida_M = datetime.datetime.now().minute

        Tempo_H = Saida_H - Entrada_H
        Tempo_M = Saida_M - Entrada_M

        if Tempo_M  < 0:
            Tempo_H -= 1
            Tempo_M = 60 - Entrada_M + Saida_M
        
        Tempo_T = (Tempo_H * 60) + Tempo_M
        return Tempo_T

    else:
        print("Os dados introduzidos são invalidos")


def Blocos15(Tempo_T:int) -> int:
    N_Blocos = (Tempo_T // 15)

    if Tempo_T % 15 != 0:
        N_Blocos += 1
    
    return N_Blocos


def Custo(Preço_Min:float, N_Blocos:int) -> float:
    return N_Blocos * Preço_Min


def main():
    Preço_Min = Preço()
    Tempo_T = Tempo()
    N_Blocos = Blocos15(Tempo_T)
    Custo_T = Custo(Preço_Min, N_Blocos)
    print (f"Terá de pagar: {Custo_T}€")

if __name__ == "__main__":
    main()