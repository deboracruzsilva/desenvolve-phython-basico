
# Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. 
# Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. 
# Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

lista1 = []
lista2 = []
while True :
    elemento = input("Digite um valor para lista 1, se quiser sair digite 'S' ou 's':")
    if elemento=="s" or elemento=='S':
        break
    lista1.append(elemento)
    

while True :
    elemento = input("Digite um valor para lista2, se quiser sair digite 'S' ou 's':")
    if elemento=="s" or elemento=='S': 
        break
    lista2.append(elemento)
    

tamanho = min(len(lista1), len(lista2))
lista3=[]
for i in range (tamanho):
      lista3.append(lista1[i])
      lista3.append(lista2[i])

lista3.extend(lista1[tamanho:]) # .extend abre a lista e adiciona os elementos individualmente
lista3.extend(lista2[tamanho:]) # o fatiamento garante que seja adicionado apenas após o término da menor lista
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista intercalada:", lista3)