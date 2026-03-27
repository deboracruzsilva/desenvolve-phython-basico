#Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. 
# Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.

nome = input("Digite seu primeiro nome :")
sobrenome = input("Digite seu sobrenome: ")
nome_completo = nome+" "+sobrenome
print(f"Bem vinda, {nome_completo}!")