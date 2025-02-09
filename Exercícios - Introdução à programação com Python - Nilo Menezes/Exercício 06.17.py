estoque={ "tomate": [ 1000, 2.30],                                                #variavel com um dicionario contendo a quantidade e o preço de cada produto
                "alface": [ 500, 0.45],
                "batata": [ 2001, 1.20],
                "feijão": [ 100, 1.50] }
venda = []                                                                        #lista vazia que servirá como um carrinho de compras
while True:                                                                       #loop para continuar inserindo itens no carrinho de compras
    nome_produto = str(input("Insira o nome do produto: "))                       #registra em uma variavel o nome do produto desejado pelo
    if nome_produto == "sair":                                                    #finaliza o programa se o usuário digitar "sair"
        break
    elif nome_produto in estoque:                                                 #verifica se o nome do produto desejado pelo usuario está no dicionario de estoque
        quantidade_produto = int(input("Agora, insira a quantidade: "))           #registra em uma variavel a quantidade desejada
        lista2 = [nome_produto, quantidade_produto]                               #registra em uma lista temporaria uma nova lista contendo o nome do produto e a quantidade
        venda.append(lista2)                                                      #insere como elemento na lista "venda" a nova lista gerada
    else:                                                                         #se o nome do produto não estiver no dicionário, informa ao usuário
        print("Produto não encontrado em nosso banco de dados")
if len(venda) > 0:                                                                #verifica se o tamanho da lista "venda" é maior que 0
    total = 0                                                                     #registra na nova variavel total o valor 0
    print("Vendas:\n")
    for operação in venda:                                                        #para cada elemento (lista) da lista "venda"
        produto, quantidade = operação                                            #divide cada elemento lista da lista venda em duas variaveis: produto e quantidade
        preço = estoque[produto][1]                                               #utiliza o nome do produto para acessar o índice 2 do chave do dicionário estoque, referente ao preço.
        custo = preço * quantidade                                                #multiplica o preço encontrado pela quantidade desejada informada pelo usuário e guardado na variavel quantidade
        print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade,preço,custo))    #imprime a operação
        estoque[produto][0] -= quantidade                                         #retira do dicionário a quantidade
        total+=custo                                                              #acrescenta na variavel total a multiplicação realizada
    print(" Custo total: %21.2f\n" % total)
    print("Estoque:\n")
    for chave, dados in estoque.items():                                          
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print("Preço: %6.2f\n" % dados[1])
else:
    print("Você encerrou o processo de compra")
