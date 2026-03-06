import re
import datetime

print(" ### Cadastramento de usuário ###")

nome = input("Insira seu nome: ")
senha = input("Insira sua senha: ")
email = input("Insira seu email: ")
# Créditos ao site GeeksForGeeks em: Check if Email Address Valid or not in Python
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
    
data_nasc = input("Insira sua data de nascimento: ")

dia = int(data_nasc[0:2])
mes = int(data_nasc[3:5])
ano = int(data_nasc[6:10])

# Créditos ao site GeeksForGeeks em: Python DateTime - Date Class
data = datetime.date(ano,mes,dia)

print("\n## Sucesso!")
print("## Nome :",nome)
print("## Senha :",senha)
print("## Email :",email)
print("## Data de nascimento :",data)
