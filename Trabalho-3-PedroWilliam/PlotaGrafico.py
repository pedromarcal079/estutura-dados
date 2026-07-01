import matplotlib.pyplot as plt
import sys

'''
Módulo para plotar gráfico conforme arquivos de resultados
autor: Arthur Souza (Modificado)
'''

def gerarGrafico(titulo, algoritmos, numeros, resultados):
    ''' 
    Gera um gráfico com o título e para os algoritmos, numeros e resultados
    obtidos dos arquivos com resultados
    '''
    # Substituído plt.figure() pela abordagem recomendada com subplots
    fig, ax = plt.subplots(figsize=(10,6))
    
    for i in range(0, len(algoritmos)):
        ax.plot(numeros, resultados[i], linewidth=4, label=algoritmos[i])        
        
    ax.set_xlabel("Tamanho da entrada (n)", fontsize=18)
    ax.set_ylabel("Tempo de execução (ms)", fontsize=18)
    ax.set_title(titulo, fontsize=18)
    ax.legend()
    ax.grid(True)
    
    # Modificação: Em vez de apenas exibir na tela (plt.show), o gráfico é 
    # salvo diretamente como imagem (.png), ideal para anexar no seu relatório.
    nome_imagem = f"{titulo.lower().replace(' ', '_')}.png"
    plt.savefig(nome_imagem, bbox_inches='tight')
    print(f"Gráfico gerado e salvo com sucesso como: {nome_imagem}")

def lendoResultados(arquivo):
    '''
    Função para ler os resultados do arquivo.
    Recebe o caminho para um [arquivo]
    Retorna um dicionário com os dados dos resultados
    algoritmo - nome do algoritmo
    n - quantidade da entrada
    resultados - dados de tempo de execução
    '''
    dados = {}
    resultados = list()
    # Adicionado encoding='utf-8' para evitar problemas de compatibilidade de SO
    with open(arquivo, 'r', encoding='utf-8') as fil:
        linha1 = fil.readline().split(";")
        dados["algoritmo"] = linha1[0]
        dados["n"] = linha1[1]
        for linha in fil:
            # Ignora linhas em branco que possam existir no final do arquivo
            if linha.strip():
                resultados.append(float(linha))
    dados["resultados"] = resultados
    return dados
    

if __name__ == "__main__":
    '''
    Lê os parametros de arquivos e gera o gráfico
    Exemplo de uso:
    python PlotaGrafico.py Fibonacci ./resultados/Fibonacci-Iterativo.res ./resultados/Fibonacci-Recursivo.res
    '''
    if len(sys.argv) > 2:
        titulo = sys.argv[1]
        algoritmos = []
        resultados = []
        n = 0
        entradasDiferentes = False
        for i in range(2, len(sys.argv)):
            dados = lendoResultados(sys.argv[i])
            algoritmos.append(dados["algoritmo"])
            resultados.append(dados["resultados"])
            nTemp = int(dados["n"])
            if (n == 0): 
                n = nTemp
            elif n != nTemp:
                entradasDiferentes = True
            # O bloco 'else: next;' original foi removido por ser redundante e incorreto em Python.

        if(not entradasDiferentes):
            # Alterado de range(0, n) para range(1, n + 1) para que as coordenadas 
            # do eixo X representem fielmente o tamanho real da entrada (de 1 até n).
            gerarGrafico(titulo, algoritmos, list(range(1, n + 1)), resultados)
        else:
            print("A quantidade das entradas dos arquivos é diferente.\nRepita o experimento para cada algoritmo com o mesmo número de entrada")

    else:
        print("Informe os parametros no formato: python PlotaGrafico.py [Título do Gráfico] [Arquivo] [Arquivo] ...")