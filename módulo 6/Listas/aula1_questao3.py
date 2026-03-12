# Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. 
# Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. 
# Ao final imprima:
# Ambas as listas
# A lista intersecção ordenada
# A quantidade de vezes que cada elemento aparece em cada lista
import random
# Cria duas listas vazias
lista1 = []
lista2 = []
# Preenche as duas listas ao mesmo tempo com números aleatórios de 0 a 50
for i in range (20):
    elementos_1 = random.randint(0,50)
    lista1.append(elementos_1)
    elementos_2 = random.randint(0,50)
    lista2.append(elementos_2)
# Imprime as duas listas
print(lista1)
print(lista2)
# Cria a lista de interseção vazia
intersecao=[]
# Preenchendo a terceira lista
for n in lista1: # percorre a lista 1
    if n in lista2 and n not in intersecao: # se na lista 2 tem o mesmo valor da lista 1 e ainda não está na lista interseção
        intersecao.append(lista1[n]) # adiciona esse valor na lista interseção
intersecao.sort() # ordena a lista sem criar duplicatas
print(intersecao) # imprime a lista interseção ordenada
# Informa quantas vezes os elementos da terceira lista aparece em cada uma das outras
for item in intersecao: # percorre a lista interseção 
    qtd1 = lista1.count(item) # conta quantas vezes o item da lista intersecao aparece na lista 1
    qtd2 = lista2.count(item) # conta quantas vezes o item da lista intersecao aparece na lista 1
    print(f"O número {item} aparece {qtd1}x na Lista 1 e {qtd2}x na Lista 2") # imprime essas informações