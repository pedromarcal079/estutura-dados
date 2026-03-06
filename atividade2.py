import re

print(" ### Cadastramento de usuário ###")

nome = input("Insira seu nome: ")
senha = input("Insira sua senha: ")
email = input("Insira seu email: ")
data_nasc = input("Insira sua data de nascimento: ")

def valida_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if re.match(regex, email):
        return True
    else:
        return False
    
if valida_email(email):
    print("Email válido")
else:
    print("Email invalido")

