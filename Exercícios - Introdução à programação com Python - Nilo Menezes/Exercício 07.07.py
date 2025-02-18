palavra = input("Digite a palavra secreta:").lower().strip()    #registra em uma variável uma palavra "secreta" informada pelo usuário
for x in range(20):                                             #imprime um ponto em 20 linhas diferentes para esconder no console a palavra digitada pelo usuário
    print(".")
digitadas = []                                                  #cria uma variável que registra uma lista para armazenar futuros caracteres informados pelo usuário
acertos = []                                                    #cria uma variável que registra uma lista para armazenar as letras futuras que serão informadas para adivinhar a composição da palavra secreta
erros = 0                                                       #cria um contador de tentativas erradas
while True:                                                     #cria um loop
    senha=""                                                    #cria uma variável com uma string vazia
    for letra in palavra:                                       #para cada caractere na palavra informada pelo usuário
        senha +=letra if letra in acertos else "."              #adiciona na variavel senha p caractere se ele estiver dentro da lista acertos; se não estiver adiciona um ponto
    if senha == palavra:                                        #se o valor string da senha for igual à palavra "secreta" informada no início pelo usuário, finaliza o programa
        print("Você acertou!")
        break
    print(senha)                                                #imprime o valor string da variavel senha, informando em que posição aquele caractere está presente na palavra secreta
    tentativa = input("\nDigite uma letra:").lower().strip()    #recebe do usuário um caractere
    if tentativa in digitadas:                                  #verifica se o caractere informado pelo usuário está presente na lista digitadas e informa o usuário se estiver
        print("Você já tentou esta letra!")
        continue
    else:        
        digitadas += tentativa                                  #adiciona à lista digitadas o caractere informado pelo usuário na variável tentativa
        if tentativa in palavra:                                #verifica se o caractere informado pelo usuário está presente na palavra secreta
            acertos += tentativa                                #se estiver, adiciona o caractere à lista acertos
        else:
            erros += 1                                          #se não estiver, aumenta em uma unidade o contador de tentativas erradas
            print("Você errou!")                                #informa ao usuario ao errar
            if erros == 6:                                      #verifica se o número de erros é igual a seis
                print("Enforcado!")
                print(f"A palavra secreta era: {palavra}")
                break                                           #se for, finaliza o programa
