#exercício 5.22

while True:                                                                                                   #cria um loop
    tabuada=1                                                                                                 #cria a variável que registra um dos fatores da tabuada
    print("Qual operação a tabuada deve apresentar? ['adição', 'subtração', 'multiplicação' ou 'divisão']")   #apresenta as opções de tabuada
    entrada=str(input(""))
    if entrada == "sair":                                                                                     #finaliza o programa se o usuário digitar "sair"
        print("Você finalizou a operação!")
        break
    elif entrada == "adição":                                                                                  #registra que a operação escolhida foi adição
        operação = "+"
    elif entrada == "subtração":                                                                               #registra que a operação escolhida foi subtração
        operação = "-"
    elif entrada == "multiplicação":                                                                           #registra que a operação escolhida foi multiplicação
        operação = "*"
    elif entrada == "divisão":                                                                                 #registra que a operação escolhida foi divisão
        operação = "/"
    else:                                                                                                      #finaliza o programa caso o usuário não digite um código válido
        print("Código inválido!")
        break
    while tabuada <=10:                                                                                        #cria um loop que permanece enquanto o primeiro fator não for igual a 10
        número = 1                                                                                             #cria a variável que registra o outro fator da tabuada
        while número <=10:                                                                                     #cria um loop que permanece enquanto o segundo fator não for igual a 10
            if operação == "+":                                                                                #soma os dois fatores, imprime o resultado da operação e aumenta em uma unidade o valor do segundo fator 
                resultado = tabuada + número
                print("%d %s %d = %d" % (tabuada, operação, número, resultado))
                número+=1
            elif operação == "-":                                                                              #subtrai os dois fatores, imprime o resultado da operação e aumenta em uma unidade o valor do segundo fator enquanto o segundo fator for menor que 10
                resultado = tabuada - número
                print("%d %s %d = %d" % (tabuada, operação, número, resultado))
                número+=1
            elif operação == "*":                                                                              #multiplica os dois fatores, imprime o resultado da operação e aumenta em uma unidade o valor do segundo fator enquanto o segundo fator for menor que 10
                resultado = tabuada * número
                print("%d %s %d = %d" % (tabuada, operação, número, resultado))
                número+=1
            elif operação == "/":                                                                              #divide os dois fatores, imprime o resultado da operação e aumenta em uma unidade o valor do segundo fator enquanto o segundo fator for menor que 10
                resultado = tabuada / número
                print("%d %s %d = %2.2f" % (tabuada, operação, número, resultado))
                número+=1
        tabuada+=1                                                                                             #após o primeiro fator chegar ao número 10, adiciona uma unidade ao valor do primeiro fator
