string1 = str(input("Digite: "))            #registra em uma variável uma string informada pelo usuário
string2 = str(input("Digite de novo: "))    #registra em outra variável outra string do usuário
string1_lista = list(string1)               #transforma cada caractere da primeira string em um elemento de uma lista
string2_lista = list(string2)               #transforma cada caractere da segunda string em um elemento de uma segunda lista
for caractere in string2_lista:             #para cada elemento da segunda lista
    if caractere in string1:                #verifica se o elemento está presente na primeira string
        string1_lista.remove(caractere)     #se estiver, remove o elemento correspondente da primeira lista
resultado = "".join(string1_lista)          #registra como uma string na variável resultado o caracteres restantes
print(resultado)                            #imprime no console (ao usuário) a string armazenada como resultado
