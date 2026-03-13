# Questão 08. Imagine um sistema de e-commerce que precisa gerenciar os itens que um usuário adiciona
# ao carrinho. Crie uma lista vazia. Adicione três produtos ("Celular", "Fone", "Capa"). O usuário desistiu
# da "Capa"; remova-a. Ao final, exiba quantos itens restaram.

carrinho = []

carrinho.append('Celular')
carrinho.append('Fone')
carrinho.append('Capa')

carrinho.pop()

print(carrinho)