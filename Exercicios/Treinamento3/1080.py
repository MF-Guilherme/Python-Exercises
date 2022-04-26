nMaior = 0
lista = []

for i in range(0, 3):
    n = int(input())
    lista.append(n)
    if n > nMaior:
        nMaior = n
print (nMaior)
print (lista.index(nMaior)+1)