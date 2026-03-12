# Atividade 01: Simule um navegador que salva o histórico de
# páginas visitadas em uma lista.

historico = []

def visitar_pagina():
    pagina = input("\nDigite a página que deseja visitar: ")
    historico.insert(0, pagina)

def ver_historico():
    print("\n5 ultimas páginas visitadas:")
    for site in historico[:5]:
        print(f"{site}")
    input("\nPressione Enter para continuar...")

def main():

    opcao = ""
    while opcao != "0":
        print("\nMenu:")
        print("1. Visitar página")
        print("2. Ver histórico")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visitar_pagina()
        elif opcao == "2":
            ver_historico()
        elif opcao == "0":
            print("Saindo do navegador...")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()