def comparação(a,b):                                    #define uma função com dois argumentos
    if a > b:                                           #veifica se o primeiro argumento é maior que o segundo
        return (a)                                      #se for, retorna ao usuário no console o primeiro argumento
    elif b > a:                                         #veifica se o segundo argumento é maior que o primeiro
        return (b)                                      #se for, retorna ao usuário no console o segundo argumento
    else:                                               #caso não atinja nenhuma das duas condições, retorna no console que os dois números são iguais
        return ("Os dois números são iguais")
print(comparação(5,6))                                  #testa a função
print(comparação(2,1))                                  #testa a função mais uma vez
print(comparação(7,7))                                  #testa a função outra vez
