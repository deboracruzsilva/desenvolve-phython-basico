with open("frase.txt","r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
# remover caracteres não alfabéticos(mantendo os espaços)
texto_limpo ="" 

for i in conteudo:
    if i.isalpha() or i ==" ":
        texto_limpo +=i

# separando as palavras
palavras = texto_limpo.split()

with open("palavras.txt","w",encoding ="utf-8") as novo_arquivo:
    for palavra in palavras:
        novo_arquivo.write(palavra+"\n")
with open("palavras.txt","r", encoding = "utf-8") as arquivo:
    print(arquivo.read())