# Sistema de entrega expressa que calcula o valor do frete com base na distância e no peso do pacote. 

# ENTRADA DE DADOS
distancia = int(input("Digite a distância em Km inteiros: "))
peso = int(input("Digite o peso do pacote em Kg: "))

# PROCESSAMENTO
if distancia<=100:
    frete = peso *1
elif distancia >100 and distancia<=300:
    frete = peso* 1.50
elif distancia>300:
    frete = peso*2
if peso> 10:
    frete += 10

# SAÍDA DE DADOS
print("Valor do frete: R$",frete)