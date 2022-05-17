qtde_testes = int(input())
i = 1

while i <= qtde_testes :
    n = int(input())
    soma = 0
    for j in range(1, n) :
        if n % j == 0 :
            soma += j
    if soma == n :
        print(f'{n} eh perfeito')
        i+=1
    else :
        print(f'{n} nao eh perfeito')
        i+=1
