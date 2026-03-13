# Questão 11. Escreva uma função Python somaTotal(numeros) que recebe uma lista de inteiros e imprime
# a soma total dos inteiros.

lista = [1,3,5,2,7,652,23,12,879]

def somaTotal(numeros):
    soma = 0
    for item in numeros:
        soma += item
    print("Soma Total: ",soma)

somaTotal(lista)
