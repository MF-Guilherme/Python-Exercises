def imprime(v):
    contador = 0
    for numero in v :
        if numero <= 10 :
            print(f'A[{contador}] = {numero:.1f}')
            contador += 1
        else:
            contador += 1

a = []
for i in range (100):
    x = float(input())
    a.append(x)
imprime(a)