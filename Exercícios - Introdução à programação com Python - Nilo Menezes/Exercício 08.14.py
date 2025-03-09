import random                                                                        #importa o módulo random
lista_de_palavras = ["arroz", "feijão", "macarrão", "salmão", "tomate", "batata"]    #registra em uma variável uma lista com seis elementos na forma de palavras
random.shuffle(lista_de_palavras)                                                    #embaralha a ordem das palavras da lista
palavra = lista_de_palavras[0]                                                       #armazena na variável "palavra" o primeiro elemento da lista recém embaralhada
for x in range(20):                                                                  #para cada valor numa faia de 1 a 20
    print()                                                                          #imprime uma linha vazia
digitadas = []                                                                       #registra na variável "digitadas" uma lista vazia
acertos = []                                                                         #registra na variável "acertos" uma outra lista vazia
erros = 0                                                                            #registra na variável "erros" o valor numérico 0, estabelecendo um contador
while True:                                                                          #estabelece um loop
    senha=""                                                                         #registra na variável "senha" uma string vazia
    for letra in palavra:                                                            #estabelece que, para cada letra da palavra armazenada na variável "palavra",
        senha +=letra if letra in acertos else "."                                   #adiciona à variável senha ou a letra correspondente, se a lista "acertos" conter tal caractere, ou um ponto, se ela não conter
    print(senha)                                                                     #imprime no console a variável "senha"  
    if senha == palavra:                                                             #estabelece que, se o valor da variável "senha" for igual ao valor da variável "palavra"
        print("Você acertou!")                                                       #imprime uma mensagem no console, informando ao usuário que ele acertou a palavra secreta
        break                                                                        #finaliza o programa
    tentativa = input("\nDigite uma letra:").lower().strip()                         #registra na variável "tentativa" um valor (caractere) informado pelo usuário
    if tentativa in digitadas:                                                       #estabelece que, se o valor da variável "tentativa" for também um elemento da lista "digitadas"
        print("Você já tentou esta letra!")                                          #informa ao usuário que o último caractere informado já foi considerado
        continue                                                                     #prossegue o programa   
    else:                                                                            #se não for,
        digitadas += tentativa                                                       #adiciona à lista "digitadas" o caractere informado pelo usuário na variável "tentativa"
        if tentativa in palavra:                                                     #e, se o valor armazenado em "tentativa" for um caractere que compõe o termo da variável "palavra"
            acertos += tentativa                                                     #adiciona à lista "acertos" o caractere em questão
        else:                                                                        #mas, se não for,
            erros += 1                                                               #aumenta em 1 unidade numérica o valor do contador "erros"
            print("Você errou!")                                                     #e informa no console ao usuário seu erro
            if erros == 6:                                                           #se o valor da variável "erros" for igual ao número 6,
                print("Enforcado!")                                                  #informa no console ao usuário que ele perdeu o jogo
                print(f"A palavra secreta era: {palavra}")                           #e apresenta no console a palavra secreta
                break                                                                #por fim, finaliza o programa
