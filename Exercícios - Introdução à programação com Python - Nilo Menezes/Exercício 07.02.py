string1 = "AAACTBF"                        #registra uma string em uma variavel
string2 = "CBTAGH"                         #registra outra string em outra variavel
string2_list = list(string2)               #transforma cada caractere da segunda string em um elemento de uma lista
resultado = []                             #cria uma lista que servirá como resultado
for caractere in string2_list:             #para cada caractere da lista composto pelos elementos da segunda string
    if caractere in string1:               #verifica se o caractere também está presente na primeira string e, se estiver, 
        resultado.append(caractere)        #adiciona o caractere na lista de resultado
print(resultado)                           #imprime o resultado
