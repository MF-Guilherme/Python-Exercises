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


m = [[1.5, 3.5, 2.0],
     [2.5, 3.5, 2.0],
     [8.5, 3.5, 2.0]
     ]
print(f'{soma(m, 0):.1f}')    
print(f'{media(m, 0):.1f}')
