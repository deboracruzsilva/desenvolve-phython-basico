# Programa que lê dois números e informa se a sua soma é par ou ímpar. 

# ENTRADA DE DADOS
numero_1 = int(input("Digite o primeiro número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))

# PROCESSAMENTO 
soma = numero_1 + numero_2 
if soma%2 == 0:
    paridade = "Par"
else:
    paridade = "Ímpar"

# SAÍDA DE DADOS
print("A soma desses dois números é ",paridade)

