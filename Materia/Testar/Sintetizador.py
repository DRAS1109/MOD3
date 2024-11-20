'''
PSI - Módulo 2
Ciclo de Repetição baseado numa condição WHILE
Programa de Login
'''
 
import random
 
print(random.randint(0,100))
 
input()
 
import winsound, time
 
pauta = input("Pauta:")
 
for nota in pauta:
   
    if (nota.upper()=='D'):
        winsound.Beep(261,500)
    elif (nota.upper()=='R'):
        winsound.Beep(293,500)
    elif (nota.upper()=='M'):
        winsound.Beep(330,500)
    elif (nota.upper()=='F'):
        winsound.Beep(349,500)
    elif (nota.upper()=='S'):
        winsound.Beep(392,500)
    elif (nota.upper()=='L'):
        winsound.Beep(440,500)
    elif (nota.upper()=='I'):
        winsound.Beep(493,500)
    elif(nota.upper==' '):
        time.sleep(500)