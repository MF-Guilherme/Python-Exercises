#ler a quantidade de casos de teste
qtde_testes = int(input())
i = 1
#cada caso de teste vai ler outras 6 entradas 
while i <= qtde_testes :
    somaJoao = 0
    somaMaria = 0
    #3 entradas para joão
    for j in range(0, 3): 
        #cada entrada terá dois valores na mesma linha separados por espaço vazio
        x, d = map(int, input().split(" "))
        #para cada entrada calcular x * d (x é a pontuação e d a distância) e acumular na soma de cada jogador
        somaJoao = somaJoao + (x * d)
    #3 entradas para maria
    for m in range(0, 3):
        x, d = map(int, input().split(" "))
        #para cada entrada calcular x * d (x é a pontuação e d a distância) e acumular na soma de cada jogador
        somaMaria = somaMaria + (x * d)
    #imprimir o vencedor de casa caso de testes
    if somaJoao > somaMaria :
        print('JOAO')
    else :
        print('MARIA')
    i+=1       