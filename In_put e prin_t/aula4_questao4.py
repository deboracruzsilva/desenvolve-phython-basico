valor = int(input("Digite qual é o valor em reais: "))
# CONTAGEM DAS NOTAS 
# Notas de 100
nota_100 = valor//100 # Divisão inteira. Ex: 576//100 = 5

# Atualiza valor para começar a contagem da próxima nota. 
valor = valor % 100 # Módulo (resto da divisão). Ex: 576 % 100 = 76.
# Notas de 50
nota_50 = valor //50 # Divisão inteira. Ex: 76//50 = 1
# Atualiza valor
valor = valor % 50 # Módulo (resto da divisão). Ex: 76 % 50 = 26
# Notas de 20
nota_20 = valor//20 # Divisão inteira. Ex: 26//20 = 1
valor = valor % 20 # Módulo (resto da divisão). Ex: 26 % 20 = 6
nota_10 = valor//10
valor = valor % 10
nota_5 = valor//5
valor = valor % 5
nota_2 = valor//2
valor = valor % 2
nota_1 = valor//1

print(f"{nota_100} nota(s) de R$100,00")
print(f"{nota_50} nota(s) de R$50,00")
print(f"{nota_20} nota(s) de R$20,00")
print(f"{nota_10} nota(s) de R$10,00")
print(f"{nota_5} nota(s) de R$5,00")
print(f"{nota_2} nota(s) de R$2,00")
print(f"{nota_1} nota(s) de R$1,00")