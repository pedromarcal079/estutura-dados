# Questão 12. O interpretador Python do computador do professor Arthur está corrompido e excluiu a
# função index(caractere) da String. Para corrigir essea falha, escreva uma função Python indice(texto,
# caractere) que recebe uma string e um caractere e retorne a posição do caractere dentro da string. de
# inteiros e imprime a soma total dos inteiros

texto = "cuscuz"

def indice(texto, caractere):
    lista = list(texto)
    i = 0
    for item in lista:
        if item == caractere:
            print("Indice: ", i)
            break
        else:
            i += 1
    if caractere not in lista: print("Nao encontrado")      

indice(texto,"a")      
