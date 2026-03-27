#Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com as letras internas de cada palavra embaralhadas. 
# Mantenha sempre o primeiro e último caractere da palavra no lugar. 
#Dica: use a biblioteca random.

import random
def embaralhar_palavras(frase):
  palavras = frase.split()
  resultado=[]
  for i in palavras:
    tam = len(i)
    if tam <= 3:
      resultado.append(i)
    else:
      embaralhe = list(i[1:tam-1]) # transforma em lista
      random.shuffle(embaralhe) # embaralha
      nova = i[0]+"".join(embaralhe)+i[-1]
      resultado.append(nova)
  return " ".join(resultado)

frase = "Python é uma linguagem de programação"
resposta = embaralhar_palavras(frase) 
print(resposta)