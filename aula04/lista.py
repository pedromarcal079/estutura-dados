# Questão 01. Qual a principal diferença entre uma Lista e uma Tupla ?
# Listas são mutáveis e tuplas são imutáveis

# Questão 02. Se você converter a lista [10, 20, 20, 30, 40, 40] em um Set, qual será o resultado final?
# Explique por que isso ocorre.
# O conjunto será {10,20,30,40}, porque conjuntos não aceitam duplicatas

# Questão 03. Dada a lista numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], utilize a acesso em sublistas para obter:
# a) Os três primeiros elementos.
# numeros[0:2]
# b) Os elementos do índice 5 ao 8.
# numeros[5:8]

# Questão 04. Dada a string texto = "banana", como você usaria um dicionário para contar quantas vezes
# cada letra aparece? (Ex: {'b': 1, 'a': 3, 'n': 2}).
# dicionario = {'b': texto.count("b"), 'a': texto.count("a"), n: texto.count("n") }

# Questão 05. Crie uma estrutura que represente uma lista de alunos, onde cada aluno é um dicionário
# contendo "nome" e uma lista de "notas". Como você acessaria a segunda nota do primeiro aluno?
# alunos = [{'nome': "Fulano", 'notas': [9,10,9.5,8,7]}]
# print(alunos[0]['notas'][1])

# Questão 06. A partir de uma lista de nomes ['ana', 'bia', 'caio'], crie um dicionário onde a chave é o nome
# e o valor é o número de letras desse nome
# nomes = ['ana', 'bia', 'caio']
# dicionario = {nomes[0]: len(nomes[0]), nomes[1]: len(nomes[1]), nomes[2]: len(nomes[2])}
# print(dicionario)

# Questão 07. Dada a lista de dicionários jogadores = [{'nome': 'A', 'pontos': 10}, {'nome': 'B', 'pontos': 50},
# {'nome': 'C', 'pontos': 30}], como você ordenaria essa lista pela pontuação (do maior para o menor)?

