"""
for i in range (10):
    print (i)
    i = 1
"""

"""
def FunçãoA():
    X = 0
    while X < 10:
        X = X + 1
        return X
    
print (FunçãoA())
print (FunçãoA())
print (FunçãoA())
"""


def FunçãoB():
    X = 0 
    while X < 10:
        X = X +1
        yield X     #Devolve o valor e mantem os estado

for i in FunçãoB():
    print(i)
    i = 0