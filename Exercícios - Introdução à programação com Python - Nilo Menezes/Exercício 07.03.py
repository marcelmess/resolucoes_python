string1 = "CTAHSOK"                                              #registra uma string qualquer em uma variavel
string2 = "ABCCLMC"                                              #registra outra string qualquer em uma segunda variavel
string3 = "BTQRS"                                                #registra outra string qualquer em terceira variavel
string1_list = list(string1)                                     #transforma os caracteres da primeira string em elementos de uma lista
string2_list = list(string2)                                     #transforma os caracteres da segunda string em elementos de uma segunda lista
string3_list = list(string3)                                     #transforma os caracteres da terceira string em elementos de uma terceira lista
resultado = []                                                   #cria uma variavel que armazena uma lista vazia para servir como resultado
for caractere in string1:                                        #para cada caractere presente na primeira string
    if caractere not in string2 and caractere not in string3:    #verifica se o caractere não está na presente na segunda string e também não está presente na terceira string
        resultado.append(caractere)                              #se não estiver, adiciona o caractere na lista da variavel resultado
for caractere in string2:                                        #para cada caractere presente na segunda string
    if caractere not in string1 and caractere not in string3:    #verifica se o caractere não está na presente na primeira string e também não está presente na terceira string
        resultado.append(caractere)                              #se não estiver, adiciona o caractere na lista da variavel resultado
for caractere in string3:                                        #para cada caractere presente na segunda string
    if caractere not in string2 and caractere not in string1:    #verifica se o caractere não está na presente na primeira string e também não está presente na segunda string
        resultado.append(caractere)                              #se não estiver, adiciona o caractere na lista da variável resultado
resultado_oficial="".join(resultado)                             #unifica em uma string armazenada em uma variável todos os elementos da lista resultado
print(resultado)                                                 #imprime ao usuário a lista contendo todos os elementos que passaram pelas condições estabelecidas
print(resultado_oficial)                                         #imprime ao usuário a string unificada com todos os elementos da lista do resultado
