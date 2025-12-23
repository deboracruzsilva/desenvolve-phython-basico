import random
numero = random.randint(1,10)
while True:
    palpite = int(input("Advinhe o número entre 1 e 10: "))
    if palpite==numero:
        print(f"Correto! O número é {numero}.")
        break
    elif palpite > numero:
        print("Muito alto, tente novamente!")
    elif palpite < numero:
        print("Muito baixo, tente novamente!")