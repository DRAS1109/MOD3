def Soma(X, Y):
    T = X + Y
    return T
    print ("Tudo o que está depois do return n é executado")


x = Soma(10, 5)
print (x)

print ("ou")

print (Soma(10, 5))

t = Soma(Soma(10, 5), 5)

print(t)