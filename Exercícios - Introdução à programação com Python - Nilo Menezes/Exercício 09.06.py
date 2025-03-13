LARGURA=79                                #registra na variável "LARGURA" um valor numérico
entrada=open("entrada.txt")               #registra na variável "entrada" a função "open", que abre um arquivo txt específico (entrada.txt)
for linha in entrada.readlines():         #estabelece que, para cada linha presente no arquivo texto da variável "entrada",
    if linha[0]==";":                     #se o primeiro elemento da linha for igual a ";"   
        continue                          #o programa continua
    elif linha[0]==">":                   #se o primeiro elemento da linha for igual a ">"
        print(linha[1:].rjust(LARGURA))   #imprime no console ao usuário o conteúdo restante da linha, adicionando, no lado esquerdo da mensagem, uma margem definida pelo valor da variável "LARGURA"
    elif linha[0]=="*":                   #se o primeiro elemento da linha for igual a "*"
        print(linha[1:].center(LARGURA))  #imprime no console ao usuário o conteúdo restante da linha, adicionando, tanto no lado esquerdo quanto no lado direito da mensagem, uma margem definida pelo valor da variável "LARGURA"
    elif linha[0]=="=":                   #se o primeiro elemento da linha for igual a "="
        print(40 * "=")                   #imprime no console ao usuário quarenta vezes o caractere "="
    elif linha[0]==".":                   #se o primeiro elemento da linah for igual a "."
        input("Aperte ENTER")             #solicita que o usuário "aperte ENTER"
    else:                                 #em qualquer outra situação,
        print(linha)                      #imprime no console ao usuário o conteúdo da linha
entrada.close()                           #fecha o arquivo que foi aberto
