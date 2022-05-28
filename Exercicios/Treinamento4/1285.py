while True :
    try :
        n, m = map(int, input().split(' '))
        contador = 0

        for numero in range(n, m + 1):
            
            numero = str(numero)
            
            if len(numero) == len(set(numero)) : #o set elimina caracteres iguais de uma string
                contador += 1
        print(contador)
    except EOFError :
        break