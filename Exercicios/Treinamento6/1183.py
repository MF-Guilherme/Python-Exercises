def soma(matriz):
    soma = 0
    i = 0
    for lista in matriz :
        soma += sum(lista[i+1:])
        i+=1
    return soma

def contagemValores(matriz) :
    
    somaContagem = 0
    cont = 0
    for lista in matriz :
        i = 0
        for valor in lista :
            i += 1
        cont += 1
        somaContagem += (i - cont)
    return somaContagem
  
def media(matriz):
    sum = soma(matriz)
    cont_valores = contagemValores(matriz)
    med = sum / cont_valores
    return med

o = input()
m = []

for i in range(12):
    lista = []
    for j in range(12):
        n = float(input())
        lista.append(n)
    m.append(lista)
if o == 'S' :
    print(f'{soma(m):.1f}')
elif o == 'M':
    print(f'{media(m):.1f}')