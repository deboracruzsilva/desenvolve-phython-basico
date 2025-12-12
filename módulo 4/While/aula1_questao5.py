n = int(input("Digite a quantidade de idades, você deseja calcular a média: "))
cont = 1
idade = 0
while cont<=n:
    idade += int(input(f"Digite a idade:{cont} "))
    cont += 1
media = idade/n
print(f"A média das idades inseridas é {media:.0f}")