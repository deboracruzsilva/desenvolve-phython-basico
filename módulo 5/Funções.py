##import random
import math
##for i in range(5):
   ## print(random.randint(0,100))

#raio = float (input("Digite o raio da circunferência: "))
#print("Sua area é %.2f"%(math.pi*raio**2))

#CRIANDO FUNÇÕES
# def minhaFuncao(parametros):
    #valor = 0
        # comandos da função
        # return valor
# programa principal

#def distancia(x,y):
   # d = math.sqrt(x**2+y**2)
   # print(d)
#print("Início")
#distancia(3,1)
#print("Fim")

#def subtracao(a,b):
#    return a-b

#s = subtracao(2,3)
#print(s)

#FUNÇÕES LAMBDA

#Anonimas com uma única expressão
# Sintaxe:
#lambda <parametros>:<expressão>
#func = lambda x:x+1
#print(func(2))

fn_maior = lambda a,b:a if a>b else b
for i in range(10):
    x,y = int(input()),int(input())
    print(fn_maior(x,y))