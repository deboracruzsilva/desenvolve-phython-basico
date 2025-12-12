print("Gênero Masculino : 'M' e gênero Femenino: 'F' ")
genero = input("Qual o seu gênero? (M ou F)")
idade = int(input("Qual a sua idade?"))
tempo = int(input("Qual o seu tempo de serviço? "))

if (genero == "F" and idade>60) or (genero =="M" and idade>65) or (tempo>=30) or (idade==60 and tempo>=25):
    aposentadoria = True
else:
    aposentadoria = False
print("Se a resposta for 'True', você está apto a se aposentar. Caso a resposta seja 'False', você não está apto a se aposentar")
print("Condição de aposentadoria:", aposentadoria)