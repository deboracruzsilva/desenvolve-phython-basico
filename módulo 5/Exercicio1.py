
def calculaFatorial(numero):
    fat = 1
    for i in range(1,numero+1):
        fat*=i
    return fat

n = int(input("Digite o valor de n: "))

fatorial = calculaFatorial(n)
print(f"{n}! é {fatorial}")