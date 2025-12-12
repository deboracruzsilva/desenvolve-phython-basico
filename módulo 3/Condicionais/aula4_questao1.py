#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. 
# Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. 
# Lembre-se do operador do python % que retorna o resto de uma divisão.

numero_1 = int(input("Digite o primeiro número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))
soma = numero_1 + numero_2 
if soma%2 == 0:
    paridade = "Par"
else:
    paridade = "Ímpar"

print("A soma desses dois números é ",paridade)

