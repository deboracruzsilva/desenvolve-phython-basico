#Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".


vogais = 'AaEeIiOoUu'
frase= input("Digite uma frase: ")
frase_mud = ""
for i in frase:
  if i in vogais:
    frase_mud+= "*"
  else:
    frase_mud += i

print(frase_mud)  