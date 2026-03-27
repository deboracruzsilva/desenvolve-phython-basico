#Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.
# ENTRADA DE DADOS
nome = input("Digite seu nome: ")
# Processamento
tam=len(nome)
resposta =""
for i in range(0, tam):
    resposta += nome[i]
    # SAÍDA
    print(resposta)