agenda = []                                                                        #registra na variável "agenda" uma lista vazia
def pede_nome():                                                                   #define uma função sem parâmetros
    return(input("Nome: "))                                                        #que retorna a convocação da função input(), solicitando ao usuário que digite o "nome"
def pede_telefone():                                                               #define uma função sem parâmetros
    return(input("Telefone: "))                                                    #que retorna a convocação da função input(), solicitando ao usuário que digite o "telefone"
def mostra_dados(nome, telefone):                                                  #define uma função com dois parâmetros: "nome" e "telefone" 
    print("Nome: %s Telefone: %s" % (nome, telefone))                              #que imprime no console os valores dos dois parâmetros
def pede_nome_arquivo():                                                           #define uma função sem parâmetros
    return(input("Nome do arquivo: "))                                             #que retorna a convocação da função input(), solicitando ao usuário que digite o "nome do arquivo"
def pesquisa(nome):                                                                #define uma função com um parâmetro
    mnome = nome.lower()                                                           #que registra na variável "mnome" a versão em caixa baixa do valor do parâmetro
    for p, e in enumerate(agenda):                                                 #e estabelece que, para cada elemento tupla da lista, que contém um número e uma lista,
        if e[0].lower() == mnome:                                                  #se o primeiro valor da lista, em caixa baixa, for igual ao valor da variável "mnome"
            return p                                                               #retorna à função o valor do primeiro valor da tupla
    return None                                                                    #e retorna mais nada
def novo():                                                                        #define uma função sem parâmetros
    global agenda                                                                  #que utliza a variável global "agenda"
    nome = pede_nome()                                                             #registra na variável local "nome" o resultado da convocação da função "pede_nome"
    telefone = pede_telefone()                                                     #registra na variável local "telefone" o resultado da convocação da função "pede_telefone"
    agenda.append([nome, telefone])                                                #adiciona à lista "agenda" uma nova lista tendo como primeiro elemento o valor da variável "nome" e o segundo elemento o valor da variável "telefone"
def apaga():                                                                       #define uma função sem parâmetros
    global agenda                                                                  #que utiliza a variável global "agenda"
    nome = pede_nome()                                                             #registra na variável local "nome" o resultado da convocação da função "pede_nome"
    p = pesquisa(nome)                                                             #registra na variável local "p" o resultado da convocação da função "pesquisa", passando como parâmetro o valor da variável "nome"
    if p!=None:                                                                    #e verifica se a valor da variável p é diferente de nada
        del agenda[p]                                                              #se for, deleta da "agenda" o valor da variável p
    else:                                                                          #se não for,
        print("Nome não encontrado.")                                              #imprime no console que o "nome não foi encontrado"
def altera():                                                                      #define uma função sem parâmetros
    p = pesquisa(pede_nome())                                                      #registra na variável local "p" o resultado da convocação da função "pesquisa", passando como parâmetro o resultado da convocação da função "pede_nome"
    if p!=None                                                                     #se o valor da variável local "p" for diferente de nada
        nome = agenda[p][0]                                                        #registra na variável local "nome" o primeiro valor da lista registrada na variável local "p"
        telefone = agenda[p][1]                                                    #registra na variável local "telefone" o segundo valor da lista registrada na variável local "p"    
        print("Encontrado:")                                                       #informa no console que o contato foi encontrado
        mostra_dados(nome, telefone)                                               #convoca a função "mostra_dados" passando como parâmetros, respectivamente, os valores registrados nas variáveis locais "nome" e "telefone"
        nome = pede_nome()                                                         #registra na variável "nome" o resultado da convocação da função "pede_nome()"
        telefone = pede_telefone()                                                 #registra na variável "telefone" o resultado da convocação da função "pede_telefone()" 
        agenda[p]=[nome, telefone]                                                 #sobreescreve a lista de "p" com uma nova lista formada pelos dois novos valores de "nome" e "telefone"
    else:                                                                          #se não for,
        print("Nome não encontrado.")                                              #informa no console que o contato não foi encontrada
def lista():                                                                       #define uma função sem parâmetros
    print("\nAgenda\n\n------")                                                    #informa no console um título
    for e in agenda:                                                               #estabelece que, para cada elemento da lista da variável "agenda",
        mostra_dados(e[0], e[1])                                                   #convoca a função "mostra_dados" passando como parâmetros o primeiro e o segundo valor do elemento lista
        print("------\n")                                                          #produz no console uma linha de separação visual
def lê():                                                                          #define uma função sem parâmetros
    global agenda                                                                  #que utiliza a variável globla "agenda"
    nome_arquivo = pede_nome_arquivo()                                             #registra na variável local "nome_arquivo" o resultado da convocação da função "pede_nome_arquivo"
    arquivo = open(nome_arquivo, "r", encoding="utf-8")                            #registra na variávle local "arquivo" o resultado da convocação da função "open" passando como parâmetros os valores apresentados entre parênteses
    agenda = []                                                                    #registra na variável global "agenda" uma lista vazia
    for l in arquivo.readlines():                                                  #estabelece que, para cada linha do arquivo de texto registrado na variável "arquivo"
        nome, telefone = l.strip().split("#")                                      #registra nas variáveis locais "nome" e "telefone" as informações da linha em consideração
        agenda.append([nome, telefone])                                            #insere na variável global "agenda" uma nova lista de contato contendo as informações de "nome" e "telefone"
        arquivo.close()                                                            #fecha o arquivo de texto aberto anteriormente
def grava():                                                                       #define uma função sem parâmetros
    nome_arquivo = pede_nome_arquivo()                                             #registra na variável local "nome_arquivo" o resultado da convocação da função "pede_nome_arquivo"
    arquivo = open(nome_arquivo, "w", encoding="utf-8")                            #registra na variávle local "arquivo" o resultado da convocação da função "open" passando como parâmetros os valores apresentados entre parênteses
    for e in agenda:                                                               #estabelece que, para cada elemento da lista da variável "agenda"
        arquivo.write("%s#%s\n" % (e[0], e[1]))                                    #escreve no arquivo de texto o primeiro e o segundo valor do elemento considerado da lista "agenda"
        arquivo.close()                                                            #fecha o arquivo de texto aberto anteriormente
def valida_faixa_inteiro(pergunta, inicio, fim):    
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <=valor <=fim:
                return(valor)
        except ValueError:
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))
def qtd_agenda():
    if len(agenda) > 1:
        print("Há %d contatos na agenda!" % (len(agenda)))
    elif len(agenda) == 1:
        print("Há um único contato na agenda!")
    else:
        print("Não há contatos na agenda.")
def menu():
    print("""
        1 - Novo
        2 - Altera
        3 - Apaga
        4 - Lista
        5 - Grava
        6 - Lê
        0 - Sai
        """)
    qtd_agenda()
    return valida_faixa_inteiro("Escolha uma opção: ",0,6)
while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()
