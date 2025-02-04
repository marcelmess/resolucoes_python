#exercício 5.23

while True:
    contador = 3                                                                                            #estabelece que o contador deve começar a contar a partir do 3
    print("Digite um número e verifique se ele é primo: ")
    entrada = int(input(""))
    status = True                                                                                           #define o status padrão para True e imprime, a não ser que o valor seja alterado, o valor como sendo primo
    if entrada == 2 or entrada == 3:                                                                        #se a entrada do usuário for igual a 2 ou 3, constata que é um número primo
        print("%d é um número primo!" % (entrada))
    else:
        while True:                                                                                         #loop
            if entrada % 2 == 0:                                                                            #verifica se o número é divisível por 2 e, se for, constata que não se trata de um número primo
                print("%d não é um número primo" % (entrada))
                break
            else:
                while contador < entrada:                                                                   #estabelece um loop que rodará que continuará ativo enquanto o contador não for igual ao número da entrada do usuário
                    if entrada % contador == 0:                                                             #executa se o resto da divisão do número pelo número atual do contador for igual a 0 e encontra o menor divisível do número da entrada do usuário
                        print("%d não é um número primo. Ele é divisível por: %d " % (entrada, contador))
                        status = False                                                                      #altera o status padrão e impede que o número seja considerado como primo
                        break
                    contador+=1                                                                             #aumenta o contador em 1 unidade
                if status:                                                                                  #imprime a entrada do usuário como um número primo após ele verificar se há algum número que consiga dividir a entrada do usuário e ter 0 como produto
                    print("%d é um número primo!" % entrada)
            break       
