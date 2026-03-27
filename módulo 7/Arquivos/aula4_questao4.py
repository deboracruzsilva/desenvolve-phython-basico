# Jogo da forca
# => gabarito_forca.txt ( arquivo com 10 palavras)
# => gabarito_enforcado.txt(conteudo apresentado ao final)

import random

with open("gabarito_forca.txt","r",encoding="utf-8") as arquivo:
    palavras = arquivo.read().splitlines()

with open("gabarito_enforcado.txt","r",encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

estagios = conteudo.split("\n\n")

def imprime_enforcado(erros):
    print(estagios[erros])

erros = 0
letra_usadas = []
palavra_sorteada = random.choice(palavras)
palavra_sorteada = palavra_sorteada.lower()
vetor = list(palavra_sorteada)
tam = len(vetor)
saida =["_"]*tam
print(" ".join(saida))

while erros <6 and "_" in saida:

    letra = input("Digite uma letra:").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("Digite apenas uma letra!")
        continue

    if letra in letra_usadas:
        print("Letra repetida, tente outra!")
        continue
    
    letra_usadas.append(letra)
    print("Letras usadas:",letra_usadas)

    if letra in vetor:
        for i in range(tam):
            if letra == vetor[i]:
                saida[i]= letra
    else:
        erros += 1
        imprime_enforcado(erros)

    print(" ".join(saida))

if "_" not in saida:
    print("Você venceu!")
else:
    print("Você perdeu! A palavra era:", palavra_sorteada)
    

