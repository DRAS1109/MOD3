import math
from datetime import datetime

#Calcula a exponenciação utilizando o operador **
def Função_Complicada():
    for i in range (100000000):
        _ = i ** 2

#Calcula a exponenciação utilizando a função pow do modulo math
def Função_Complicada2():
    for i in range (100000000):
        _ = math.pow(i, 2)

def Tempo():
    Inicio = datetime.now()
    Função_Complicada()
    Fim = datetime.now()
    Tempo_Execução = Fim - Inicio
    print ("Tempo de execução: ", Tempo_Execução.total_seconds())

    Inicio = datetime.now()
    Função_Complicada2()
    Fim = datetime.now()
    Tempo_Execução2 = Fim - Inicio
    print (print ("Tempo de execução 2: ", Tempo_Execução2.total_seconds()))

Tempo()


