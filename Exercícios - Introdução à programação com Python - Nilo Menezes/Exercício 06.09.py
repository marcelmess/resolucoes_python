L=[15,7,27,39]                                        #cria uma lista com 4 valores
p=int(input("Digite o primeiro valor a procurar: "))  #recebe do usuário um primeiro valor
p2=int(input("Digite o segundo valor a procurar: "))  #recebe do usuário um segundo valor
x=0                                                   #cria um contador com valor inicial igual a 0
while x<len(L):                                       #estabelece um loop que permanece ativo enquanto o contador for menor que o tamanho da lista L
    if L[x]==p:                                       #verifica se o índice da lista, indicado pelo valor atual do contador, é igual ao primeiro valor recebido pelo usuário
        print("%d achado na posição %d" % (p,x))      #imprime o índice onde o valor foi encontrado
        break                                         #finaliza o programa
    elif L[x]==p2:                                    #verifica se o índice da lista, indicado pelo valor atual do contador, é igual ao segundo valor recebido pelo usuário
        print("%d achado na posição %d" % (p2, x))    #imprime o índice onde o valor foi encontrado
        break                                         #finaliza o programa
    x+=1                                              #aumenta em 1 unidade o valor do contador
