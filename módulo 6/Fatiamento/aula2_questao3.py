# Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. 
# Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. 
# Você deve imprimir a lista antes e depois da deleção.
import random
lista = []
for i in range(20):
    elemento = random.randint(-10,10)
    lista.append(elemento)

print("Original:",lista)
inicio_maior, tam_maior = 0, 0 # inicializa o indice do inicio da maior fatia, e o tamanho dela
inicio_atual, tam_atual = 0, 0 # inicializa o indice da fatia que está sendo avaliada no momento do laço, e o tamanho dela
for i in range(len(lista)): # percorre a lista
    if lista[i]<0: # se o elemento atual for negativo
        if tam_atual == 0:
            inicio_atual = i # o inicio atual recebe o indice
        tam_atual +=1 # a contagem de quantidade de números negativos começa
    else: # se não, se for positivo ou zero
        if tam_maior<tam_atual: # se o tamanho da mior fatia for menor que o da atual
            tam_maior = tam_atual # o tamanho da maior fatia receebe o tamanho da atual
            inicio_maior = inicio_atual # e o indice do inicio tambem
        tam_atual = 0 # zera a contagem do tamanho da fatia atual
if tam_atual > tam_maior: # confere para caso o ultimo elemento da lista seja negativo
    tam_maior = tam_atual
    inicio_maior = inicio_atual
if tam_maior:
    del lista[inicio_maior:inicio_maior+tam_maior]
print("Editada:",lista )