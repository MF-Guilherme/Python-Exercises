v = int(input()) #Ler um numero inteiro
#adicionar esse número na lista
n = [v]
#rodar 10 vezes
for i in range (10):
    mult = n[i] * 2 #pegar o numero lido e multiplicar por 2
    n.append(mult) #adicionar esse número na lista
    print(f'N[{i}] = {n[i]}') #pra cada posição da lista imprimir o índice e o valor