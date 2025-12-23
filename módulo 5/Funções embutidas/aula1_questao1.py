##Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais 
# e calcule a diferença absoluta entre esses dois números. 
# Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para 
# arredondar o resultado para duas casas decimais.
num_1= float(input("Digito o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
diferenca = abs(num_1-num_2)
print("A diferença absoluta entre os números é: ", round(diferenca,2))