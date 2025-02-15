string1 = "TTAACHUJSILAJSDJHISDH"                                                     #registra uma string em uma variável base                                                    
resultado=[]                                                                          #cria uma lista vazia cujos futuros elementos comporão o resultado do programa
for caractere in string1:                                                             #para cada caractere da string da varaivel base
    if caractere in string1 and caractere not in resultado:                           #verifica se o caractere também não está presente na lista resultado
        resultado.append(caractere)                                                   #se não estiver, inclui o caractere na lista, que estará composta apenas por elementos únicos
registro = []                                                                         #cria uma lsita vazia que servirá para armazenar a quantidade de cada caractere presente na string
for caractere in resultado:                                                           #para cada caractere único na lista resultado
    registro.append(string1.count(caractere))                                         #armazena na lista registro a quantidade de vezes que o caractere aparece na string da variavel base                                                 #
contador = 0                                                                          #cria uma variavel que atuara como um contador
for caractere in resultado:                                                           #para cada caractere único presente na lista resultado
    print("Há %d unidades da letra %s" % (registro[contador], caractere))             #imprime ao usuário a quantidade, armazenada na lista registro, do mesmo caractere na string 
    contador+=1                                                                       #aumenta em uma unidade o valor do contador, permitindo que o programa informe o número adequado correspondente ao caractere que foi armazenado na lista registro
