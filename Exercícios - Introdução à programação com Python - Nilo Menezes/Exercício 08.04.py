def cálculo (b, a):            #estabelece uma função que recebe dois parâmetros
    return ((b*a)/2)           #retorna a divisão do produto da multiplcação do segundo parâmetro pelo primeiro parâmetro
n1 = int(input("Base: "))      #registra em uma variável um primeiro valor numérico informado pelo usuário
n2 = int(input("Altura: "))    #registra em uma outra variável um segundo valor numérico informado pelo usuário
print(cálculo(n1, n2))         #imprime no console o resultado da convocação da recém criada função, utilizando os dois valores numéricos informados pelo usuário como dois parâmetros diferentes
