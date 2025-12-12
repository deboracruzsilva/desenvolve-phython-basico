idade = int(input("Digite a sua idade: "))
qntd_jogos = input("Já jogou pelo menos 3 jogos? (True ou False) ")
vitorias = int(input("Quantos jogos já venceu? "))


if qntd_jogos.lower()=="true" or "True":
    jogou3 = True
else:
    jogou3 = False

if idade>=16 and idade<= 18 and jogou3 == True and vitorias>1:
    apto = True
else:   
    apto = False


print("Apto para ingressar no clube de jogos de tabuleiro: ",apto)