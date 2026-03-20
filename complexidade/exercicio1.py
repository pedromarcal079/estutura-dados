def pesquisaLista(lista,elemento):
    cont = 0
    for num in lista:
        if num == elemento: 
            cont += 1
    return cont

def contaLista(lista):                               # 1
    repetidos = set()                                # 2  
    for i in range(0,len(lista)):                    # 3
        for j in range(0,len(lista)):                # 4
            if i != j and (lista[i] == lista[j]):    # 5
                repetidos.add(lista[i])              # 6
    return repetidos                                 # 7
        