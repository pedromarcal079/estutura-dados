"""
Módulo: main.py
Execução e monitoramento de tempo para os arquivos de inserção, busca e remoção.
"""
import time
import csv
import os
from HashTable import HashTableEnderecamentoLivre, HashTableEncadeamentoArvore

def carregar_dados_csv(caminho_arquivo, apenas_chave=False):
    dados = []
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return dados
        
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo, delimiter=',')
        next(leitor, None)  # Pula o cabeçalho
        for linha in leitor:
            if not linha:
                continue
            if apenas_chave:
                dados.append(linha[0])  # CPF
            else:
                # CPF, Dicionário com Dados Pessoais
                dados.append((linha[0], {"nome": linha[1], "sobrenome": linha[2], "idade": linha[3]}))
    return dados

def executar_experimento(nome_hash, tabela_objeto, dados_insercao, dados_busca, dados_remocao):
    print(f"\n--- Iniciando Experimento: {nome_hash} ---")
    os.makedirs('resultados', exist_ok=True)
    
    # 1. Monitoramento da Inserção
    tempos_insercao = []
    for cpf, pessoa in dados_insercao:
        inicio = time.perf_counter()
        tabela_objeto.adicionar(cpf, pessoa)
        fim = time.perf_counter()
        tempos_insercao.append((fim - inicio) * 1000)
        
    # 2. Monitoramento da Busca
    tempos_busca = []
    for cpf in dados_busca:
        inicio = time.perf_counter()
        tabela_objeto.buscar(cpf)
        fim = time.perf_counter()
        tempos_busca.append((fim - inicio) * 1000)
        
    # 3. Monitoramento da Remoção
    tempos_remocao = []
    for cpf in dados_remocao:
        inicio = time.perf_counter()
        tabela_objeto.remover(cpf)
        fim = time.perf_counter()
        tempos_remocao.append((fim - inicio) * 1000)

    # Salvando os resultados no formato padrão .res
    salvar_res(f"{nome_hash}-Insercao", tempos_insercao)
    salvar_res(f"{nome_hash}-Busca", tempos_busca)
    salvar_res(f"{nome_hash}-Remocao", tempos_remocao)

def salvar_res(nome_arquivo, tempos):
    caminho = os.path.join('resultados', f"{nome_arquivo}.res")
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(f"{nome_arquivo};{len(tempos)}\n")
        for t in tempos:
            f.write(f"{t:.6f}\n")
    print(f"Salvo: {caminho}")

if __name__ == "__main__":
    # Carrega os arquivos enviados pelo professor (certifique-se de que estão na mesma pasta)
    print("Carregando arquivos CSV...")
    dados_ins = carregar_dados_csv("insercao.csv", apenas_chave=False)
    dados_bsc = carregar_dados_csv("busca.csv", apenas_chave=True)
    dados_rmv = carregar_dados_csv("remocao.csv", apenas_chave=True)
    
    if dados_ins:
        # Executa para Endereçamento Livre
        hash_livre = HashTableEnderecamentoLivre(capacidade=15000)
        executar_experimento("HashLivre", hash_livre, dados_ins, dados_bsc, dados_rmv)
        
        # Executa para Encadeamento por Árvores Binárias
        hash_arvore = HashTableEncadeamentoArvore(capacidade=1000)
        executar_experimento("HashArvore", hash_arvore, dados_ins, dados_bsc, dados_rmv)
        
        print("\nExperimentos concluídos! Arquivos prontos na pasta /resultados.")