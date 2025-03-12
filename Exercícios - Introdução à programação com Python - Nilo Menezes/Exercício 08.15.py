import types                                    #importa o módulo "types"
lista=[1,[2,3,4,[5,6,7,[8,9,10]]]]              #registra na variável "lista" uma lista que contém como elemento uma outra lista que, por sua vez, contém uma outra lista que, por sua vez, contém outra lista que, por fim, contém outra lista, todas com alguns elementos numéricos
def função(b, contador):                        #estabelece uma função que recebe dois parâmetros
    for a in b:                                 #estabelece que para cada elemento do primeiro parâmetro   
        if type(a)==int:                        #se o tipo do elemento for int (numérico inteiro)
            print((contador * " ") + (str(a)))  #informa ao usuário no console uma mensagem contendo, primeiro, um número de espaços multiplicado pelo valor do segundo parâmetro, seguido da versão string do elemento considerado
        else:                                   #se não for,
            função(a, contador + 4)             #convoca a função, definindo o elemento em questão como o primeiro parâmetro e o segundo elemento, adicionado de 4 unidades, como o segundo parâmetro
função(lista, 0)                                #convoca a função criada, definindo como o valor da variável lista como o primeiro parâmetro e o valor numérico 0 como o seu segundo parâmetro
