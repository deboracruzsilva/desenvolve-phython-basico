#Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). 
# Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. 
# Seu programa deve continuar rodando até que o usuário digite "Fim".

while True:
  frase = input("Digite uma frase: ")
  nova=""
  if frase!= 'fim':
    for i in frase.lower():
      if i.isalpha():
        nova += i
    if nova == nova [::-1]:
      print(f'"{frase}" é palíndromo.')
    else:
      print(f'"{frase}" não é palíndromo.')
  else: 
      break
