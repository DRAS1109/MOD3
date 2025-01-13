def Triangulo():
    N = int(input("Qual o tamanho da base: "))

    for i in range(1, N +1):
        print(i * "*")

def Criptografar():
    Alfabeto = "abcdefghijklmnopqrstuvwxyz"
    Numero = 0

    Palavra  = input("Qual palavra pretende criptografar: ")

    for f in range (len(Palavra)):
        for i in range (26):
            if Alfabeto[i] == Palavra[f].lower():
                print(i + 1)

def Alfabeto():
    import numpy as np
    N = int(input("Quantas letras deve ter o Array? "))

    Arrai = np.empty(N,dtype="U1")

    Alfabeto = "abcdefghijklmnopqrstuvwxyz"

    for i in range (N):
        Arrai[i] = Alfabeto[i].upper()
    
    print(Arrai)

def Ano():
    import datetime
    Ano_Atual = (datetime.date.today().year)
    if Ano_Atual % 4 == 0:
        print("Eá bissexto")
    else:
        print("Ano comum")

def Numeros():
    import numpy as np
    Numeros  = input("Introduza um numero: ")
    Resultado = np.empty((len(Numeros)),dtype="U1")
    
    for i in range(len(Resultado)):
        Resultado[i] = Numeros[i]

    for i in range(len(Resultado)):
        for j in range(i + 1, len(Resultado)):
            if Resultado[i] > Resultado[j]:
                Temporario = Resultado[j]
                Resultado[j] = Resultado [i]
                Resultado[i] = Temporario

    print(f"Numeros ordenados: {Resultado}")


#Triangulo()
#Criptografar()
#Alfabeto()
#Ano()
Numeros()