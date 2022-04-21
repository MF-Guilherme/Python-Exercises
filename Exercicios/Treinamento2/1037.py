numero = float(input())
intervalo = ['Intervalo [0,25]','Intervalo (25,50]', 'Intervalo (50,75]', 'Intervalo (75,100]', 'Fora de intervalo']

if numero >= 0 and numero <= 25:
    print(intervalo[0])
elif numero > 25 and numero <= 50:
    print(intervalo[1])
elif numero > 50 and numero <= 75:
    print(intervalo[2])
elif numero > 75 and numero <= 100:
    print(intervalo[3])
else:
    print(intervalo[4])
