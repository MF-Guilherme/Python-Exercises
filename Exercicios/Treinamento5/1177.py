t = int(input())
n = []
cont = 0
while len(n) < 1000 :
    for valor in range (0, t) :
        n.append(valor)
        if len(n) <= 1000 :
            print(f'N[{cont}] = {valor}')
            cont += 1
        