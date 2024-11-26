import datetime

Dia = int(input("Dia da nascimento: "))
Mes = int(input("Mes da nascimento: "))
Ano = int(input("Ano da nascimento: "))

Hoje = datetime.datetime.today()

Data_Nascimento = datetime.date(Ano, Mes, Dia)

#Calcular Idade

Idade = Hoje.year - Data_Nascimento.year

#Verificar se fez anos
if Data_Nascimento.month > Hoje.month or (Data_Nascimento.month == Hoje.month and Data_Nascimento.day > Hoje.day):
    Idade -= 1

print (Idade)