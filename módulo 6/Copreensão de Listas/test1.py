# Map e Filter
# MAP
# sintaxe => map(função, iterável , iterável2,..., iterável_n)
def fn_quadrado(n):return n**2
lista =[2,3,5,7]
#quadrado = map(fn_quadrado,lista)
quadrado =  map(lambda n: n**2, lista) # objeto gerador, não produz resultados instantaneamente
#for item in quadrado:
    #print(item, end=' ')
print(list(quadrado))# para converter e ter um retorno
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
soma =  map(lambda x,y:x+y, lista1, lista2)
print(list(soma))

areas = [3.567,5.5768,4.014,56.241,9.344]
#areas = map(round,areas)
areas = map(round,areas,[2]*len(areas)) # pecisão de dois
print(lista(areas))

#FILTER
# sintaxe => filter(função, iterável)
# pede uma função que retorna uma expressão boleana
# def testa_sinal(n):return n>0 
listas = [-2,3,-5,7]
positivos = filter(lambda z:z>0, listas)
print(list(positivos))
