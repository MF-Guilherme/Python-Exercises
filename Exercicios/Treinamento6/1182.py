def media(matriz, coluna) :
    cont = 0
    soma = 0
    for lista in matriz :
        soma += lista[coluna]    
        cont += 1
    med = soma / cont
    return med

def soma(matriz, coluna) :
    soma = 0
    for lista in matriz :
        soma += lista[coluna]
    return soma

c = int(input())
t = input()
m = []

for i in range(3):
    lista = []
    for j in range(3):
        n = float(input())
        lista.append(n)
    m.append(lista)
if t == 'S' :
    print(f'{soma(m, c):.1f}')
elif t == 'M':
    print(f'{media(m, c):.1f}')