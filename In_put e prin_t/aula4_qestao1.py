
# Nesse código o objetivo é calcular o valor do terreno e a área dele, a aprtir de suas dimensões.

# ENTRADA DE DADOS
# Entrada do valor do comprimento em metros do terreno. Variável do tipo inteiro.
comprimento = int(input('Qual é o comprimentro em metros do seu terreno:'))

# Entrada do valor da largura do terreno em metros. Variável do tipo inteiro.
largura = int(input('Qual é a largura do seu terreno:'))

# Entrada do preço de cada metro quadrado do terreno, Variável do tipo float.
preco_m2 = float(input('Qual é o preço do metro quadrado da região:'))

# CÁLCULOS
# Calculo da area total em metros quadrados do terreno. Variável do tipo inteiro.
area_m2 = comprimento * largura
# Calculo do preco total do terreno em reais.
preco_total = preco_m2 * area_m2

#SAÍDA DE DADOS
# Saída de dados para o usuário
print(f"O terreno possui {area_m2}m² e custa R$ {preco_total}.")