# Compreensão de listas
# sintaxe => resultado = [expressâo for item in lista] 
lista = [2,3,5,7]
#quadrado = []
#for n in lista:
    #quadrado.append(n**2)
# com compreensão de listas
quadrado = [n**2 for n in lista]
print(quadrado)
# Exemplo : primeiro eçemento de cada lista dentro das listas
listas =[[1,2,3],[4,5,6],[7,8,9]]
itens = [l[0] for l in listas]
print(itens)
# com condicionais
# sintaxe=> resultado = [expressão for item in lista if condição]
# Exemplo : selecionar números positivos de uma lista
nums = [-21,12,14,-37,-9,20]
positivos=[n for n in nums if n>0]
print(positivos)
# exemplo : testar interceções entre listas
lista1 = [30,40,70,80,110]
inters = [l for l in lista1 if l in [20,70,110,140]]
print(inters)
# turbinando com else
# sintaxe => resultado = [exp_true if condição else exp_false for item in lista]
# Exemplo, truncar valores negativos de uma lista
filt = [l if l>=0 else 0 for l in nums]
print(filt)