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

m = [[1.5, 3.5, 2.0, 7.8, 9.0],
     [2.5, 3.5, 2.0, 1.8, 6.9],
     [8.5, 3.5, 2.0, 8.4, 2.8],
     [8.5, 3.5, 2.0, 8.6, 2.8],
     [8.5, 3.5, 4.9, 8.4, 2.8],
     ]

print(media(m))