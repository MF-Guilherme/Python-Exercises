def media(lista) :
    cont = 0
    soma = 0
    for valor in lista :
        soma += valor    
        cont += 1
    med = soma / cont
    return med

l = int(input())
t = input()
m = []

for i in range(12):
    lista = []
    for j in range(12):
        n = float(input())
        lista.append(n)
    m.append(lista)
if t == 'S' :
    print(f'{sum(m[l]):.1f}')
elif t == 'M':
    print(f'{media(m[l]):.1f}')