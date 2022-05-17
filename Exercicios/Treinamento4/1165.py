qtde_testes = int(input())
i = 1

while i <= qtde_testes :
    multiplos = 0
    n = int(input())
    for j in range(2, n+1) :
        if n % j == 0 :
            multiplos += 1
    if multiplos == 1 :
        print(f'{n} eh primo')
        i+=1

    else:         
        print(f'{n} nao eh primo')
        i+=1
