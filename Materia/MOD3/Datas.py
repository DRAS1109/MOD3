import datetime

#Data de hoje
print(datetime.date.today())

#Ano
print(datetime.date.today().year)

#Mes
print(datetime.date.today().month)

#Dia
print(datetime.date.today().day)

print("\n")

#Data em Hora
print(datetime.datetime.now())

    #Hora
print(datetime.datetime.now().hour)

    #Minuto
print(datetime.datetime.now().minute)

    #Segundo
print(datetime.datetime.now().second)

#Data como String
print(datetime.datetime.now().strftime("%d - %m - %Y %H:%M:%S"))