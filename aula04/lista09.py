# Questão 09. Um mercadinho quer saber quantos quilos de cada fruta tem em estoque. Crie um
# dicionário com {"maçã": 10, "banana": 15}. Atualize o estoque de "banana" para 20 e adicione "uva"
# com 5. No final, imprima apenas as chaves (nomes das frutas) disponíveis.

estoque = {
    'maçã': 10,
    'banana': 15
}

estoque['banana'] = 20
estoque['uva'] = 5

print(estoque.keys())