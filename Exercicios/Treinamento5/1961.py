p, n = map(int, input().split(' '))
lista = input().split()
cont = 0
caiu = 0

for i in range(len(lista)):
    lista[i] = int(lista[i])

while cont < len(lista):
    if cont + 1 < len(lista) :
        if abs(lista[cont] - lista[cont+1]) > p :
            caiu += 1
            cont += 1
        else :
            cont += 1
    else:
        cont += 1    
if caiu == 0 :
    print('YOU WIN')    
else: 
    print('GAME OVER')
  