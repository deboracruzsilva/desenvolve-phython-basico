import random
import math
n = int(input("Digite o valor de n: "))
soma = 0
for i in range(n):
    soma += random.randint(0,100)
resultado = math.sqrt(soma)
print(f"A raiz quadrada da soma de {n} números aleatórios é: {resultado}")