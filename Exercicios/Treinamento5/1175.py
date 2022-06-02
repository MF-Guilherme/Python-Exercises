def inverter_lista(lista) :
    cont = 0
    lista_inversa = []
    for valor in reversed(lista):
        lista_inversa.append(valor)
        print(f'N[{cont}] = {valor}')
        cont += 1

n = []
for i in range (20) :
    x = int(input())
    n.append(x)
inverter_lista(n)