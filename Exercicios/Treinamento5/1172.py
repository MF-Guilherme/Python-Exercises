x = []
contador = 0
i = 0

while contador < 10 :
    n = int(input())
    if n <= 0 :
        x.append(1)
    else :
        x.append(n)
    contador += 1
for valor in x :
    print(f'X[{i}] = {valor}')
    i+=1
    
