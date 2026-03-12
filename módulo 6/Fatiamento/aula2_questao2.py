# Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", 
# use o conceito de fatiamento de listas para criar uma lista dominios com o nome principal de todos os domínios, conforme exemplo a seguir. 
# URLs: ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
# dominios:  ["google", "gmail", "github", "reddit", "yahoo"]
urls= ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios=[]
for url in urls:
    site = url [4:-4]
    dominios.append(site)
print("URLs: ",urls)
print("Dominios",dominios)