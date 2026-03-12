# Atividade 02: Numa clínica médica os pacientes são
# atendidos por ordem de chegada. Implemente esse controle

fila_pacientes = []

def inserir_paciente():
    nome = input("\nDigite o nome do paciente: ")
    fila_pacientes.append(nome)
    print(f"Paciente {nome} adicionado à fila.")


def chamar_proximo_paciente():
    if fila_pacientes:
        paciente = fila_pacientes.pop(0)
        print(f"Chamando o próximo paciente: {paciente}")
    else:
        print("Não há pacientes na fila.")
    input("Pressione Enter...")


def main():
    opcao = ""
    while opcao != "0":
        print("\nMenu:")
        print("1. Chegada do paciente")
        print("2. Chamar próximo paciente")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_paciente()
        elif opcao == "2":
            chamar_proximo_paciente()
        elif opcao == "0":
            print("Saindo...")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()