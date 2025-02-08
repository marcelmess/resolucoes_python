lista = [5, 10, 36, 76, 93, 3, 24, 55]    #estabelece uma lista com alguns valores (int)
fim = len(lista)                          #registra na variavel fim o tamanho da lista como um valor
while fim > 1:                            #estabelece um loop que permanece enquanto a variavel fim for maior que 1
    trocou = False
    x = 0                                 #estabelece um contador, que inicia com o valor 0
    while x<(fim-1):                      #estabelece um loop que permanece enquanto o contaodr for menor que o tamanho da lista menos 1 unidade
        if lista[x] < lista[x+1]:         #verifica se o valor da lista indicado pelo indice do valor respectivo do contador é menor que o valor seguinte da lista
            trocou = True                 #se for, registra na variavel "trocou" o valor booleano true
            temp = lista[x]               #salva o valor da lista indicado pelo idndice do valor do contador em questão
            lista[x] = lista[x+1]         #altera o valor da lista indicado pelo idndice do valor do contador em questão pelo valor seguinte da lista
            lista[x+1] = temp             #altera o valor seguinte da lista para o valor guardado na variável "temp"
        x+=1                              #aumenta em 1 unidade o valor do contador
    if not trocou:                        #se a variável trocou não estiver com o valor True, então o loop finaliza
        break
for valor in lista:                       #imprime cada valor da lista, um de cada vez
    print(valor)
