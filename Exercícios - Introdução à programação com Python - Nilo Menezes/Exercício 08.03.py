def cálculo(a):                #estabelece uma função que recebe um parâmetro
    return (a*a)               #retorna a multiplicação do parâmetro pelo próprio parâmetro
área = int(input("Número: "))  #registra em uma variável um valor numérico informado pelo usuário
print(cálculo(área))           #imprime no console o resultado da convocação da função cálculo tendo como parâmetro o valor numérico registrado na variável área
