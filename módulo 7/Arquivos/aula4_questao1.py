import os # biblioteca para lidar com os caminhos

frase = input("Digite uma frase: ")
# cria e abre o arquivo para escrita
with open("frase.txt","w", encoding ="utf-8") as arquivo:
  # escreve a frase no arquivo
  arquivo.write(frase)
# pega o caminho completo do arquivo
caminho = os.path.abspath("frase.txt")
print(f"Arquivo salvo em:\n {caminho}")