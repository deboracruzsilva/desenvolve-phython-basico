# Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. 
# Em seguida imprima na ordem estabelecida:
# A lista ordenada, sem modificar a lista original
# A lista original
# O índice do maior valor da lista
# O índice do menor valor da lista

import random # importa a biblioteca random
l1 = [] # cria uma lista vazia
for i in range(20): # laço que preenche a lista com 20 números aleatórios
    l=random.randint(-100,100) # cria uma variável que armazena o numero escolhido entre -100 e 100
    l1.append(l) # adiciona a lista
l1_ord = sorted(l1) # pega a lista preenchida com números aleatórios e ordena e armazena em outra lista
print("Lista ordenada: ",l1_ord) # imprime a lista ordenada
print("Lista original:",l1) # imprime a lista original
ind_maior = l1.index(max(l1)) # pega o indice do maior número na lista
maior = l1[ind_maior] # o maior recebe o valor que contém esse indice
print("Índice do maior valor da lista original: ",ind_maior) # imprime o indice
print(maior) # imprime o valor
# o mesmo para o indice de menor valor
ind_menor = l1.index(min(l1)) 
menor = l1[ind_menor]
print("Índice do menor valor da lista original:",ind_menor)
print(menor)