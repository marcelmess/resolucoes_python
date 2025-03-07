def validacao(minimo, maximo):                                #estabelece uma função com dois parâmetros
    while True:                                               #estabelece um loop
        entrada = str(input("Insira a string: "))             #registra em uma variável uma valor string do usuário
        if minimo > len(entrada) or maximo < len(entrada):    #verifica se o número de caracteres da variável criada é menor que o primeiro parâmetro ou maior que o segundo parâmetro
        else:
            return entrada                                    #se não for, a função retorna o valor da variável 
print(validacao(3, 20))                                       #imprime no console a convocação da função, definindo como parâmetros os valores "3" e "20"
