import re
import datetime



print('###  cacdastro de usuario ###\n')

nome = input('Digite o nome do usuario\n')
senha = input('Digite a idade do usuario\n')


data_nasc = input('Digite a data de nascimento (dd/mm/aa):\n')

dia = int(data_nasc[0:2])
mes = int(data_nasc[3:5])
ano = int(data_nasc[6:10])

data_nasc = datatime.data(ano,mes,dia)
    
# em desenvolvimento
#email = input('Digite o email do usuario\n')


print('##Cadastro realizado com sucesso!##\n')

print('nome:', nome,)
print('idade:', senha)
print('Data de nascimento:', data_nasc)