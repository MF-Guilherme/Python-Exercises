soma = 0
qtd = 0
n = 0
while n >= 0: 
    n = int(input()) 
    if n < 0:
        break   
    else:
        soma+=n
        qtd+=1
media = soma / qtd
print(f'{media:.2f}')