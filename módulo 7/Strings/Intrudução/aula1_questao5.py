#Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou". Exemplo:
#Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
#19 vogais
#Índices [1, 2, 4, 6, 10, 12, 14, 18, 20, 22, 25, 28, 29, 31, 35, 37, 40, 44, 46]

frase = input("Digite uma frase: ")
vogais ='AaEeIiOoUu'
cont = 0
indices = []
for i in range(0,len(frase)):
  if frase[i] in vogais:
    cont+=1
    indices.append(i)

print(f"=> {cont} vogais;")  
print(f"=>índices: {indices}")