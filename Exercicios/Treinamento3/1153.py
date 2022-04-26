n = int(input())
fatorial = 1
lista = []
for i in range(n, 0,-1):
    lista.append(i)
for num in lista:
    fatorial*=num
print(fatorial)