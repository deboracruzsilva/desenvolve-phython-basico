# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
# Dica: usando listas você não precisa fazer um "if" para cada mês.

meses = ['0','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho', 'Agosto', 'Setembro','Outubro','Novembro','Dezembro']

nascimento = input("Digite uma data de nascimento no formato\n => DD/MM/AAAA: ")
dia = nascimento[0:2]
mes = nascimento[3:5]
ano = nascimento[6:]
mes_int = int(mes)

if 1 <= mes_int <= 12:
    mes_ext = meses[mes_int]
    print(f"Você nasceu em {dia} de {mes_ext} de {ano}.")
else:
    print("Data inválida.")