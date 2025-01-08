def validacao(minimo, maximo):
    while True:
        entrada = str(input("Insira a string: "))
        if minimo > len(entrada) or maximo < len(entrada):
            return False
        else:
            return entrada

print(validacao(3, 20))