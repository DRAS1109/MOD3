from datetime import datetime
import time

Despertou = False
Minutos = 0

while True:
    print (datetime.now())
    #Esperar 1 segundo
    time.sleep(60)
    Minutos = Minutos + 1
    if Minutos == 5:
        break

#Despertador
while True:
    Hora_Atual = datetime.now().strftime("%H:%M:%S")
    time.sleep(1)
    if Despertou == True:
        print ("A aula acabou")
    
    if datetime.now().hour >= 16 and datetime.now().minute >= 35:
        Despertou = True