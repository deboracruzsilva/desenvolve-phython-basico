#Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.
#Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
#Digite a palavra objetivo: amor
#Anagramas: ["amor", "mora", "ramo", "Roma"] 
frases = input("Digite uma frase: ")
palavra = input("Digite a palavra objetivo: ")
lista_palavras = (frases.lower()).split()
anagrama =[]
palavra_ordenada = sorted(palavra.lower())
for i in lista_palavras:
  if len(palavra)==len(i):
    if sorted(i) == palavra_ordenada:
      anagrama.append(i)

print("Anagramas: ",anagrama)

