# Verifica se os pontos são coerentes com a classe escolhida pelo usuário.

# ENTRADA DE DADOS
classe = input("Escolha a classe (guerreiro, mago, ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# PROCESSAMENTO
escolha = False

if classe == "mago" :
    escolha = (forca<=10) and (magia>=15)

elif classe == "guerreiro" :
    escolha = (forca>=15) and (magia<=10)

elif classe == "arqueiro" and forca&magia>5 and forca&magia<=15:
    escolha = (forca>5 and forca<=15) and (magia>5 and magia<=15)

else:
    escolha = False

# SAÍDA DE DADOS
print("Pontos de atributo consistentes com a clase escolhida: ",escolha)