#ENTRADA DE DADOS
#Entrada do nome do usário
nome = input("Digite o nome do usuário: ")

# Entrada dos produtos
# Produto 1
prod_1 = input("Digite o nome do produto 1: ") # Nome do produto
pre_prod_1 = float(input("Digite o preço unitário do produto 1: ")) # Preço unitário do produto
qnt_prod_1 = int(input("Digite a quantidade do produto 1: ")) # Quantidade do produto

# Produto 2
prod_2 = input("Digite o nome do produto 2: ") # Nome do produto
pre_prod_2 = float(input("Digite o preço unitário do produto 2: ")) # Preço unitário do produto
qnt_prod_2 = int(input("Digite a quantidade do produto 2: ")) # Quantidade do produto

# Produto 3
prod_3 = input("Digite o nome do produto 3: ") # Nome do produto
pre_prod_3 = float(input("Digite o preço unitário do produto 3: ")) # Preço unitário do produto
qnt_prod_3 = int(input("Digite a quantidade do produto 3: ")) # Quantidade do produto

# CÁLCULO DO VALOR TOTAL
total = (pre_prod_1*qnt_prod_1) + (pre_prod_2*qnt_prod_2) + (pre_prod_3*qnt_prod_3) # Soma do produto dos preços unitários e das quantidades

# SAÍDA
print(f"Total: R$ {total:,.2f} ")

