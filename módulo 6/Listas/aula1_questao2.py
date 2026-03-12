# Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. 
# Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:
# A lista elementos
# A soma dos valores da lista
# A média dos valores da lista
import random 
num_elementos = random.randint(5,20) # define de forma aleatoria o número de elementos que a lista terá
elementos =[] # lista vazia
soma=0
 # preenche a lista com números aleatorios
for i in range(num_elementos): 
    elemento = random.randint(1,10)
    elementos.append(elemento)
print(elementos)
soma = sum(elementos) # soma todos os elementos da lista
print(soma)
media = soma/len(elementos) # faz a media dividindo a soma pelo tamanho da lista
print(f"{media:.2f}") # imprime a lista
