from Utils import Ler_Inteiro
from Ex03_Primo import Primo

X = Ler_Inteiro()
Y = Ler_Inteiro()

if Primo(X) == True and Primo(Y) == True:
    if abs(X - Y) == 2:
        print("São Nº primos gémeos")
    else:
        print("São Nº primos")

else:
    if Primo(X) == True:
        print(f"O valor {X} é primo")
    
    if Primo(Y) == True:
        print(f"O valor {Y} é primo")