# Sistema de classificação de filmes com base nas avaliações dos usuários. 

# ENTRADA DE DADOS
filme = input("Digite o nome do filme a ser avaliado: ")
avaliacao = int(input("Digite a sua avaliação desse filme em uma escala de 1 a 5: "))

# PROCESSAMENTO
if avaliacao== 5:
    classificacao = "Excelente"
elif avaliacao == 4:
    classificacao = "Muito Bom!"
elif avaliacao == 3:
    classificacao = "Bom!"
elif avaliacao == 2:
    classificacao = "Regular."
elif avaliacao == 2:
    classificacao = "Ruim."

# SAÍDA DE DADOS
print("A clasifição desse filme é: ",classificacao)
