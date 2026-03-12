# Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase (remova espaços em branco)
frase = input("Digite uma frase:")
vogais_set = ['A','a','E','e','I','i','O','o','U','u']
consoantes_set = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vogais=[letra for letra in frase if letra in vogais_set ]
vogais.sort()
print("Vogais:",vogais)
consoantes = [l for l in frase if l in consoantes_set]
print("Consoantes:",consoantes)