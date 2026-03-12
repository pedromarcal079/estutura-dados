# Atividade 03: Uma empresa mantém registros de funcionários
# com acesso ao sistema administrativo e ao sistema financeiro.

listaAdministrativo = {'Pedro', 'Luis', 'Bia', 'Helena'}
listaFinanceiro = {'Isabelle', 'Pedro', 'Helena', 'Bia', 'Andriel'}

def ambos_sistemas():
    ambos = listaAdministrativo.intersection(listaFinanceiro)
    print("\nUsuarios com acesso a ambos os sistemas")
    for user in ambos:
        print(f"{user}")

def apenas_um_sistema():
    apenas_admin = listaAdministrativo.difference(listaFinanceiro)
    apenas_finan = listaFinanceiro.difference(listaAdministrativo)
    
    print("\nUsuarios com acesso a apenas o sistema administrativo")
    for user in apenas_admin:
        print(f"{user}")
    print()
    print("Usuarios com acesso a apenas o sistema financeiro")
    for user in apenas_finan:
        print(f"{user}")

def todos_usuarios():
    todos = listaAdministrativo.union(listaFinanceiro)
    print("\nTodos os usuarios com acesso aos sistemas")
    for user in todos:
        print(f"{user}")
    


def main():
    opcao = ""
    while opcao != "0":
        print("\nMenu:")
        print("1. Acesso a ambos os sistemas")
        print("2. Acesso a apenas um dos sistemas")
        print("3. Todos os usuários com acesso aos sistemas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ambos_sistemas()
            input("Pressione Enter...")
        elif opcao == "2":
            apenas_um_sistema()
            input("Pressione Enter...")
        elif opcao == "3":
            todos_usuarios()
            input("Pressione Enter...")
        elif opcao == "0":
            print("Saindo...")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()