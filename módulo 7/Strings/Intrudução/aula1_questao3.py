#Escreva um script que dado uma frase conta os espaços em branco.
#Digite a frase: Meu amor mora em Roma e me deu um ramo de flores
#Espaços em branco: 11

frase = input("Digite uma frase: ")
cont_espacos = 0
tam = len(frase)
for i in range(tam):
    if frase[i] == " ":
        cont_espacos+=1
print("Espaços em branco:", cont_espacos)