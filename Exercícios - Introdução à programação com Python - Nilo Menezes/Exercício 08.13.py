import random                                            #realiza a importação do módulo random
n=random.randint(1,10)                                   #registra na variável "n" um valor aleatório entre 1 e 10
for caractere in range(3):                               #estabelece que, para cada caractere numa faixa com três valores
    x = int(input("Escolha um número entre 1 e 10:"))    #registra na variável "x" um valor numérico informado pelo usuário
    if x==n:                                             #verifica se o valor de "x" é igual ao valor de "n"
        print("Você acertou!")                           #se for, informa ao usuário que o número é o mesmo 
        break                                            #e finaliza o programa
    else:                                                #se não for, informa que o usário errou o número secreto
        print("Você errou.")
