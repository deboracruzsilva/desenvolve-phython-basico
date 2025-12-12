N = int(input("Digite o número de experimentos: "))
i = 0
S = 0
R = 0
C = 0

while i<N :
    qntd_cobaias = int(input("Digite quantas cobaias: "))
    print("S:Sapo, R:Rato ou C:Coelho")
    tipo_cobaia = input("Qual tipo('S', 'R' ou 'C'): ")
    if tipo_cobaia == "S":
        S += qntd_cobaias

    elif tipo_cobaia == "R":
        R += qntd_cobaias

    elif tipo_cobaia == "C":
        C += qntd_cobaias
    
    i += 1

total = S + R + C
percentual_C = (C/total)*100
percentual_R = (R/total)*100
percentual_S = (S/total)*100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")
print(f"Percentual de coelhos: {percentual_C:.2f} %")
print(f"Percentual de ratos: {percentual_R:.2f} %")
print(f"Percentual de sapos: {percentual_S:.2f} %")