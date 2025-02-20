lista_de_palavras = ["arroz", "feijão", "macarrão", "salmão", "tomate", "batata"]       #cria uma lista com algumas palavras como elementos
entrada = int(input("Digite um número:"))                                               #registra em uma variável um valor numérico informado pelo usuáio
índice = (entrada * 776) % len(lista_de_palavras)                                       #registra em uma variável um número mais ou menos aleatório
palavra = lista_de_palavras[índice]                                                     #registra em uma variável o elemento da lista de palavras correspondente no indice ao valor aleatório 
for x in range(30):                                                                     #imprime 30 linhas vazias para esconder o número de entrada do usuário no console
    print()
digitadas = []                                                                          #registra em uma variável uma lista vazia que armazenará futuros letras como elementos
acertos = []                                                                            #registra em uma variável uma lista vazia que armazenará as letras digitadas pelo usuário que estiver na palavra do elemento escolhido da lista de palavras
erros = 0                                                                               #registra em uma variável o valor numérico zero, criando um contador
while True:                                                                             #estabelece um loop
    senha=""                                                                            #registra em uma variável uma string vazia que servirá de senha
    for letra in palavra:                                                               #para cada letra da palavra selecionada da lista
        senha +=letra if letra in acertos else "."                                      #adiciona a letra corresponde se a letra estiver na lista de acertos e, se não estiver, adiciona um ponto
    print(senha)                                                                        #imprime ao usuário a senha, mostrando as letras acertadas
    if senha == palavra:                                                                #se a senha for igual à palavra, informa que o usuário acertou a palavra e finaliza o programa
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()                            #registra na variável tentativa uma letra informada pelo usuário
    if tentativa in digitadas:                                                          #se a letra informada pelo usuário já estiver na lista de letras digitadas, informa ao usuário
        print("Você já tentou esta letra!")
        continue
    else:                                                                               #se não estiver,
        digitadas += tentativa                                                          #adiciona a letra à lista de letras digitas
        if tentativa in palavra:                                                        #se a letra digitada estiver na palavra selecionada
            acertos += tentativa                                                        #adiciona à lista de acertos a letra digitada
        else:                                                                           #se não estiver,
            erros += 1                                                                  #adiciona ao contador uma unidade numérica
            print("Você errou!")                                                        #e informa ao usuário que a letra não consta na palavra selecionada
            if erros == 6:                                                              #se o contador chegar ao número seis, finaliza o programa
                print("Enforcado!")
                print(f"A palavra secreta era: {palavra}")
                break
