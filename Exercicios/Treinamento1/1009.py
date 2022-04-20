nome = input()
salarioFixo = float(input())
totalDeVendas = float(input())
salarioFinal = totalDeVendas*0.15 + salarioFixo
print('TOTAL = R$', '%.2f'%salarioFinal)