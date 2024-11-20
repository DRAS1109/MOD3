# Arredondamentos
import math #importar a biblioteca de funções math

X = 11.5

print(int(X)) #Converte para o numero inteiro sem arredondar
print(round(X)) #Arredonda para o número par mais proximo

print(math.ceil(X)) # arredonda sempre para o inteiro seguinte (para cima)
print(math.floor(X)) # arredonda sempre para o inteiro anterior (para baixo)

#Arredondar para cima se a parte decimal >= 0.5
parte_decimal = X - (int(X))
if parte_decimal >= 0.5:
    X = int(X) + 1
else:
    X = int(X)
print(X)