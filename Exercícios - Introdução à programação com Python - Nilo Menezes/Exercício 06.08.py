lista=[15,7,27,39]                                    #cria uma lista com alguns valores
p=int(input("Digite o valor a procurar:"))        #recebe do usuário um valor, o qual deve ser procurado na lista
x=0                                               #cria uma contador
while x<len(L):                                   #elabora um loop que permanece enquanto o contador for menor que o tamanho da lista
    if lista[x]==p:                               #verifica se o valor do usuário está no índice indicado pelo contador. se estiver, informa a posição do valor na lista e finaliza o programa
        print("%d achado na posição %d" % (p,x))
        break                                
    x += 1                                        #aumenta em 1 unidade o valor do contador, permitindo, por conta do loop, que o valor do usuário seja procurado em cada índice da lista (até encontrá-lo)
