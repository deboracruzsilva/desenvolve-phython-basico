#Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:
#Chave de criptografia: gere um valor n aleatório entre 1 e 10
#Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)
#nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
#chave_aleatoria = 5
#nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']

import random

def encrypt(lista_nomes):
  chave = random.randint(1,10)
  resultado = []
  
  for nome in lista_nomes:
    nome_crip = ""
    for caractere in nome:
      codigo = ord(caractere)
      if 33<= codigo <=126:
        inicio = 33
        total = 94 
        novo_codigo = (codigo - inicio + chave) % total + inicio
        nome_crip += chr(novo_codigo)
      else:
        nome_crip += caractere

    resultado.append(nome_crip)      
  return resultado,chave

nomes = ["Luana","Ju","Davi","Vivi","Pri","Luiz"]
resposta, chave_alt = encrypt(nomes)

print(f"Nomes: {nomes}")
print(f"Chave aleatória: {chave_alt}")
print(f"Nomes criptografados: {resposta}")
