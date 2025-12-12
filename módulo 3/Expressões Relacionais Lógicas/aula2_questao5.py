# Verifica se usúario está nas condições adequadas de se aposentar.

print("Gênero Masculino : 'M' e gênero Femenino: 'F' ") # Breve explicação para facilitar entendimento do usuário.

# ENTRADA DE DADOS
genero = input("Qual o seu gênero? (M ou F)") 
idade = int(input("Qual a sua idade?"))
tempo = int(input("Qual o seu tempo de serviço? "))

# PROCESSAMENTO
if (genero == "F" and idade>60) or (genero =="M" and idade>65) or (tempo>=30) or (idade==60 and tempo>=25):
    aposentadoria = True
else:
    aposentadoria = False

print("Se a resposta for 'True', você está apto a se aposentar. Caso a resposta seja 'False', você não está apto a se aposentar")
 # Breve explicação para facilitar entendimento do usuário.

# SAÍDA
print("Condição de aposentadoria:", aposentadoria)