# Código para validar entrada de duas pessoas maiores de idade em um bar
# ENTRADA DE DADOS
# Faz a entrada das idades de Juliana e Cris
idade_1 = int(input("Digite a idade do cliente 1: ")) # Converte a entrada idade para um tipo inteiro.
idade_2 = int(input("Digite a idade do cliente 2: ")) # Igual ao anterior.
# PROCESSAMENTO
if idade_1>17 and idade_2>17: # Verifica se ambas as idades são maiores que 18.
    print(True) # Se sim elas estão liberadas e a resposta é 'True'.
else:
    print(False) # Se não, elas não estão liberadas e a resposta é 'False'.