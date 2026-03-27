#Desenvolva um validador de CPF. 
# Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido".

cpf = input("Digite seu cpf no formato:\nXXX.XXX.XXX.-XX:")
# remove pontos e traços
cpf_limpo = cpf.replace(".","").replace("-","")

# verifica tamanho e se só tem números
if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
  print("Inválido")
else:
  #transforma em lista de inteiros usando compreensâo de lista
  numeros = [int(d) for d in cpf_limpo]

# primeiro digito
soma = 0
multiplicador = 10

for i in range(9):
  soma += numeros[i]* multiplicador
  multiplicador -= 1
resto = soma%11
digito1 = 0 if resto <2 else 11 - resto

# segundo digito
soma = 0
multiplicador = 11

for i in range(10):
  soma += numeros[i]* multiplicador
  multiplicador -= 1
resto = soma%11
digito2 = 0 if resto < 2 else 11 -resto

if digito1 == numeros[9] and digito2 == numeros[10]:
  print("Válido")
else:
  print("Inválido")




  

