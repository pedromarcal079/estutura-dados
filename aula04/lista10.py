# Questão 10. Escreva uma função Python imprimeLista(lista) que recebe uma lista de elementos e
# imprime todos os elementos.

teste = ['luis', 'pedro']

def imprimeLista(lista):
    for item in lista:
        print(f"{item}")

imprimeLista(teste)