def F_Cel(Fahr):
    Cel = (Fahr-32)*5/9
    print(f"{Fahr}° Fahrenheit são {Cel}° Celcius")

def C_Fahr(Cel):
    Fahr = (9*Cel/5) + 32
    print(f"{Cel}° Celcius são {Fahr}° Fahrenheit")

F_Cel(50)
C_Fahr(10)