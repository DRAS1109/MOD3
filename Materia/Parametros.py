def Somar (x, y):
    print (x + y)
    x = 0
    y = 0

def main():
    Somar("Joaquim", "Maria")
    Somar(10, 5)
    Somar(10.3, -3.2)
    n = 10
    z = 15
    Somar (n, z)
    print (n, z)

if __name__ == '__main__':
   main() 

def Saudacao (texto="Mundo"):
    print(f"Olá {texto}")

Saudacao("Joaquim")
Saudacao()

def Saudacao2 (Parte_Dia, Nome = "Joaquim"):
    print (f"{Parte_Dia}, {Nome}")

Saudacao2("Boa Tarde")
Saudacao2("Boa Tarde", "Ana")
Saudacao2(Nome = "Ana", Parte_Dia = "Boa Tarde")