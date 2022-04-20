A, B, C = map(float, input().split(" "))

trianguloRetangulo = (A * C) / 2
circulo = 3.14159 * (C * C)
trapezio = ((A + B) * C) / 2
quadrado = B * B
retangulo = A * B
print('TRIANGULO:', '%.3f'%trianguloRetangulo)
print('CIRCULO:', '%.3f'%circulo)
print('TRAPEZIO:', '%.3f'%trapezio)
print('QUADRADO:', '%.3f'%quadrado)
print('RETANGULO:', '%.3f'%retangulo)

""" valor = input().split(" ")
A, B, C = valor

trianguloRetangulo = (float(A) * float(C)) / 2
circulo = 3.14159 * (float(C) * float(C))
trapezio = ((float(A) + float(B)) * float(C)) / 2
quadrado = float(B) * float(B)
retangulo = float(A) * float(B)
print('TRIANGULO:', '%.3f'%trianguloRetangulo)
print('CIRCULO:', '%.3f'%circulo)
print('TRAPEZIO:', '%.3f'%trapezio)
print('QUADRADO:', '%.3f'%quadrado)
print('RETANGULO:', '%.3f'%retangulo) """

