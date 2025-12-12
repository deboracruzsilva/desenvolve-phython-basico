#Nesse código deseja se verificar se há pelo menos uma pessoa maior de idade para permitir a entrada no bar.
# ENTRADA DE DADOS
# Faz a entrada das idades de Juliana e Cris
idade_1 = int(input("Digite a idade do cliente 1: ")) # Converte a entrada idade para um tipo inteiro.
idade_2 = int(input("Digite a idade do cliente 2: ")) # Igual ao anterior.
# PROCESSAMENTO
if idade_1>17 or idade_2>17: # Verifica se uma das idades é maior que 18.
    print(True) # Se pelo menos um cliente for maior de idade, elas estão liberadas e o programa irá imprimir :'True'.
else:
    print(False) # Se nenhuma dos dois clientes for maior de idade então não estão liberadas e o programa irá iprimir: 'False'.