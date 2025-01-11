agenda = []
def pede_nome():
    return(input("Nome: "))
def pede_telefone():
    return(input("Telefone: "))
def pede_data():
    return(input("Data: "))
def pede_email():
    return(input("Email: "))
def mostra_dados(índice, nome, data, email, telefone):
    print("Nome: %s \nTelefone: %s \nData de aniversário: %s \nEmail: %s \nÍndice: %s" % (nome, telefone, data, email, índice))
def pede_nome_arquivo():
    return(input("Nome do arquivo: "))
def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None
def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    data = pede_data()
    email=pede_email()
    agenda.append([nome, telefone, data, email])
def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p!=None:
        print("A informação será apagada. Continuar?")
        confirmação = int(input("Se sim, digite 1. Se não, digite 2."))
        if confirmação == 2:
            print("Apagamento cancelado!")
        else:
            del agenda[p]
    else:
        print("Nome não encontrado.")
def altera():
    p = pesquisa(pede_nome())
    if p!=None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        data=agenda[p][2]
        email=agenda[p][3]
        print("Encontrado:")
        mostra_dados(p, nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        data = pede_data()
        email=pede_email()
        print("A informação será alterada. Continuar?")
        confirmação = int(input("Se sim, digite 1. Se não, digite 2."))
        if confirmação == 1:
            agenda[p] = [nome, telefone, data, email]
        else:
            print("Alteração cancelada.")
    else:
        print("Nome não encontrado.")
def lista():
    print("\nAgenda\n\n------")
    for e in agenda:
        mostra_dados(agenda.index(e), e[0], e[1], e[2], e[3])
        print("------\n")
def lê():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    agenda = []
    for l in arquivo.readlines():
        nome, telefone, data, email = l.strip().split("#")
        agenda.append([nome, telefone, data, email])
        arquivo.close()
def grava():
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda:
        arquivo.write("%s#%s#%s#%s\n" % (e[0], e[1], e[2], e[3]))
        arquivo.close()
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