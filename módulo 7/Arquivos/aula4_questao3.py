
# Abre o arquivo
with open("Shrek_o_musical.txt","r",encoding ="utf-8") as arquivo:
    linhas = arquivo.readlines() # lê linha por linha do arquivo
print("Primeiras linhas")
for linha in linhas[:25]:
    print(linha.strip())
    #Imprime as primeiras 25 linhas

num_linhas = len(linhas)
print("Número de linhas do arquivo:",num_linhas)

linha_maior = max(linhas,key=len)
print("Linha com maior número de caracteres:",linha_maior.strip())
print("Quantidade de caracteres:",len(linha_maior))

texto_completo ="".join(linhas).lower()

palavras = texto_completo.split()

contador_fiona = palavras.count("fiona")
contador_shrek = palavras.count("shrek")

print("Fiona:",contador_fiona)
print("Sherek:",contador_shrek)