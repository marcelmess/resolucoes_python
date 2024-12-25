#exercício 5.23

while True:
    print("Digite um número e verifique se ele é primo: ")
    entrada = int(input(""))
    contador = 3
    verificação1 = entrada % 2
    status = False
    if entrada == 2:
        print("%d é um número primo!" % (entrada))
    else:
        while True:
            if verificação1 == 0:
                status = True
                
                print("%d não é um número primo" % (entrada))
            else:
                contador = 1
                while contador >= entrada:
                    operação = entrada % contador
                    if operação == 0:
                        status = True
                        print("%d não é um número primo" % (entrada))
                        break
                    contador += 1
            break
        if status == False:
            print("%d é um número primo!" % (entrada))
