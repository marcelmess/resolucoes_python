#estoque
estoque={ "tomate": [ 1000, 2.30],
                "alface": [ 500, 0.45],
                "batata": [ 2001, 1.20],
                "feijão": [ 100, 1.50] }
#carrinho de compras
venda = []

#loop para continuar inserindo itens no carrinho de compras
while True:
    nome_produto = str(input("Insira o nome do produto: "))
    if nome_produto == "sair":
        break
    elif nome_produto in estoque:
        quantidade_produto = int(input("Agora, insira a quantidade: "))
        lista2 = [nome_produto, quantidade_produto]
        venda.append(lista2)
    else:
        print("Produto não encontrado em nosso banco de dados")

#condição para o cálculo e a impressão
if len(venda) > 0:
    total = 0
    print("Vendas:\n")

#iteração do cálculo para cada produto
    for operação in venda:
        produto, quantidade = operação
        preço = estoque[produto][1]
        custo = preço * quantidade
        print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade,preço,custo))
        estoque[produto][0] -= quantidade
        total+=custo

#impressão do resultado
    print(" Custo total: %21.2f\n" % total)
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print("Preço: %6.2f\n" % dados[1])
else:
    print("Você encerrou o processo de compra")