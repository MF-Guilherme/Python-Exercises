n1, n2, n3, n4 = map(float, input().split(" "))
m1 = 2
m2 = 3
m3 = 4
m4 = 1
mediaPonderada = ((n1 * m1) + (n2 * m2) + (n3 * m3) + (n4 * m4)) / (m1 + m2 + m3 + m4)

print('Media:', '%.1f' % mediaPonderada)

if mediaPonderada >= 7.0 :
    print('Aluno aprovado.')
elif mediaPonderada < 5.0 :
    print('Aluno reprovado.')
elif mediaPonderada >= 5.0 and mediaPonderada <= 6.9 :
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame:', '%.1f' % exame)
    mediaFinal = (exame + mediaPonderada) / 2
    if mediaFinal >= 5.0 :
        print('Aluno aprovado.')
    elif mediaFinal < 4.9 :
        print('Aluno reprovado.')
    print('Media final:', '%.1f' % mediaFinal)