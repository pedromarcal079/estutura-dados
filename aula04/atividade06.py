rank = {
    1: {"nome": "Alice",
        "pontos": 1500
    },
    2: {"nome": "Bob",
        "pontos": 1200
    },
    3: {"nome": "Charlie",
        "pontos": 900
    }
}

def inserir_jogador():
    nome = input("\nDigite o nome do jogador: ")
    pontos = int(input("Digite os pontos do jogador: "))
    rank[len(rank) + 1] = {"nome": nome, "pontos": pontos}
    print(f"Jogador {nome} adicionado ao ranking.")

def atualizar_pontos():
    posicao = int(input("\nDigite a posição do jogador a atualizar: "))
    if posicao in rank:
        pontos = int(input("Digite os novos pontos do jogador: "))
        rank[posicao]["pontos"] = pontos
        print(f"Pontos do jogador {rank[posicao]['nome']} atualizados para {pontos}.")
    else:
        print("Posição inválida.")

def exibir_ranking():
    print("\nRanking dos jogadores:")
    for posicao, jogador in rank.items():
        print(f"{posicao}. {jogador['nome']} - {jogador['pontos']} pontos")

def main():
    opcao = ""
    while opcao != "0":
        print("\nMenu:")
        print("1. Inserir novo jogador")
        print("2. Atualizar pontos de jogador")
        print("3. Exibir ranking")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_jogador()
            input("Pressione Enter...")
        elif opcao == "2":
            atualizar_pontos()
            input("Pressione Enter...")
        elif opcao == "3":
            exibir_ranking()
            input("Pressione Enter...")
        elif opcao == "0":
            print("Saindo...")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()