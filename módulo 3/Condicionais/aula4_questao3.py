# Um programa que verifica se um ano é bissexto. 

# ENTRADA DE DADOS
ano = int(input("Digite algum ano (Ex: 2025): "))

# PROCESSAMENTO 
if ano%4 == 0 and ano%100!=0 or ano%400==0:
    resposta = "Bissexto"
else:
    resposta ="Não Bissexto"

# SAÍDA DE DADOS
print("O ano é: ", resposta)