def soma(L):                        #estabelece uma função denominada "soma" que recebe um parâmetro 
    total=0                         #na função, registra em uma variável o valor numérico 0
    for i in L:                     #estabelece que para cada elemento da lista passada pelo parâmetro da função
        total+=i                    #adiciona o valor do elemento à variável total
    return total                    #retorna o valor numérico armazenado na variável total
lista=[1,7,2,9,15]                  #registra em uma variável uma lista com 5 valores numéricos diferentes
print(soma(lista))                  #imprime no console o resultado da convocação da função soma utilizando como parâmetro a variável criada com a lista
print(soma([7,9,12,3,100,20,4]))    #imprime no console o resultado da convocação da função soma utilizando como parâmetro uma nova lista com 7 valores numéricos
