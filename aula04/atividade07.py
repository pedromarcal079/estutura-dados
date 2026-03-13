# Atividade 07: Considere um cadastro de Cliente/Usuário.

# 1. Crie um código para verificar o TELEFONE.
def verificar_telefone(telefone):
    # 00 9 1234 5678
    if len(telefone) != 11 or telefone.isalpha():
        return False
    return True

def ler_telefone():
    while True:
        telefone = input("Insira um numero de telefone: ")
        if not verificar_telefone(telefone):
            print("Numero de telefone precisa ter 11 digitos")
            continue
        break
    return telefone

# 2. Crie um código para verificar a DATA de Nascimento.
def verificar_data_nascimento(data):
    if len(data) != 10: return False
    if data[2] != '/' or data[5] != '/': return False
    dia = data[0:2]
    mes = data[3:5]
    ano = data[6:10]
    if dia.isnumeric() and mes.isnumeric() and ano.isnumeric():
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        if (1 <= dia <= 31 and 1 <= mes <= 12 and ano > 1900):
            return True
    return False

def ler_data_nascimento():
    while True:
        data = input("informe a data de nascimento (dd/mm/aaaa): ")
        if not verificar_data_nascimento(data):
            print("A data de nascimento informada não é válida.\nExemplo de data válida: 01/01/2000")
            continue
        break
    return data

# 3. Crie um código para verificar se a Senha tem: uma
# maiúscula, uma minúscula, um número, um caractere
# especial e tamanho mínimo de 6.
def verificar_senha(senha):
    if len(senha) < 6 or senha.islower() or senha.isupper() or senha.isalpha() or senha.isdigit(): return False
    if not senha.isprintable(): return False
    return True

def ler_senha():
    while True:
        senha = input("informe a senha: ")
        if not verificar_senha(senha):
            print("A senha deve ter uma maiúscula, uma minúscula, um número, um caractere especial e tamanho mínimo de 6")
            continue
        break
    return senha


def main():
    opcao = ""
    while opcao != "0":
        print("\nMenu:")
        print("1. Verifica telefone")
        print("2. Verifica data de nascimento")
        print("3. Verifica senha")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ler_telefone()
            input("Pressione Enter...")
        elif opcao == "2":
            ler_data_nascimento()
            input("Pressione Enter...")
        elif opcao == "3":
            ler_senha()
            input("Pressione Enter...")
        elif opcao == "0":
            print("Saindo...")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()