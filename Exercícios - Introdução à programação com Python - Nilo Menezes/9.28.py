agenda = []
def pede_nome():
    return(input("Nome: "))
def pede_telefone():
    número = input("Número: ")
    tipo = int(input("Tipo: "))
    if tipo == 1:
        return (str(número) + " - Fixo")
    if tipo == 2:
        return (str(número) + " - Celular")
    if tipo == 3:
        return (str(número) + " - Trabalho")
    if tipo == 4:
        return (str(número) + " - Fax")
def pede_data():
    return(input("Data: "))
def pede_email():
    return(input("Email: "))
def mostra_dados(índice, nome, telefone, telefone2, telefone3, data, email):
    print("Nome: %s \nTelefone: %s \nTelefone 2: %s \nTelefone 3: %s \nData de aniversário: %s \nEmail: %s \nÍndice: %s" % (nome, telefone, telefone2, telefone3, data, email, índice))
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
    telefone2 = pede_telefone()
    telefone3 = pede_telefone()
    data = pede_data()
    email= pede_email()
    agenda.append([nome, telefone, telefone2, telefone3, data, email])
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
        telefone2 = agenda[p][2]
        telefone3 = agenda[p][3]
        data=agenda[p][4]
        email=agenda[p][5]
        print("Encontrado:")
        mostra_dados(p, nome, telefone, telefone2, telefone3, data, email)
        nome = pede_nome()
        telefone = pede_telefone()
        telefone2 = pede_telefone()
        telefone3 = pede_telefone()
        data = pede_data()
        email=pede_email()
        print("A informação será alterada. Continuar?")
        confirmação = int(input("Se sim, digite 1. Se não, digite 2."))
        if confirmação == 1:
            agenda[p] = [nome, telefone, telefone2, telefone3, data, email]
        else:
            print("Alteração cancelada.")
    else:
        print("Nome não encontrado.")
def lista():
    print("\nAgenda\n\n------")
    for e in agenda:
        mostra_dados(agenda.index(e), e[0], e[1], e[2], e[3], e[4], e[5])
        print("------\n")
def lê():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    agenda = []
    for l in arquivo.readlines():
        nome, telefone, telefone2, telefone3, data, email = l.strip().split("#")
        agenda.append([nome, telefone, telefone2, telefone3, data, email])
        arquivo.close()
def grava():
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda:
        arquivo.write("%s#%s#%s#%s\n" % (e[0], e[1], e[2], e[3], e[4], e[5]))
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