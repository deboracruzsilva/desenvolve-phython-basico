# Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), 
# os armazena em uma lista e, usando fatiamento de listas, imprima:
# A lista original
# Os 3 primeiros elementos
# Os 2 últimos elementos
# A lista invertida (do fim para o começo)
# Os elementos de índice par (0, 2, 4 … )
# Os elementos de índice ímpar (1, 3, 5, … )

lista = []
while True :
    elemento = int(input("Digite um valor:"))
    lista.append(elemento)
    if len(lista)>4:
        resposta = input("Se deseja sair digite 0 se não digite qualquer coisa:")
        if resposta=="0":
            break


print(lista[:3])
print(lista[-2:])
print(lista[0::-1])
print(lista[::2])
print(lista[1::2])
