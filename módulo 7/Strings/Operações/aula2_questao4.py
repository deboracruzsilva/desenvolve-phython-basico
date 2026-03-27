#Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
# => Pelo menos 8 caracteres de comprimento.
# => Contém pelo menos uma letra maiúscula e uma letra minúscula.
# => Contém pelo menos um número.
# => Contém pelo menos um caractere especial (por exemplo, @, #, $).

def validador_senha(senha):
  especiais = "@#$%&*!?"
  if (
      len(senha)>=8 
      and any(x.isupper()for x in senha) 
      and any(x.islower()for x in senha) 
      and any(x.isdigit() for x in senha)
      and any(x in especiais for x in senha)
  ):
    return True 
  return False

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))# True
print(validador_senha(senha2))# false
print(validador_senha(senha3))# false
