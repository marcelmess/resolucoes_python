while True:                        #estabelece um loop
    n1 = int(input("Número 1: "))  #registra em uma variável um número informado pelo usuário
    n2 = int(input("Número 2: "))  #registra em uma outra variável um segundo número informado pelo usuário
    def múltiplo(a, b):            #estabelece uma função que recebe dois parãmetros (a, b)
        if (a%b==0):               #verifica se o resto da divisão do primeiro parâmetro pelo segundo é igual a zero
            return True            #se for, retorna a função como verdadeiro
        else:                      #se não for, retorna a função como falso
            return False
    print(múltiplo(n1, n2))        #imprime no console o resultado da função criada considerando como parâmetros os dois números informados pelo usuário que foram registrados nas duas variáveis.
