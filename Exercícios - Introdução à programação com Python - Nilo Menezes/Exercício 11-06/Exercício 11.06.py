import sqlite3


entrada=input("Nome do produto: ")
entrada2=input("Novo valor: ")
conexão = sqlite3.connect("preços.db")
cursor = conexão.cursor()
cursor.execute("update preços set preço = ? where nome = ?", (entrada2, entrada))
cursor.execute("select * from preços where nome = ?", (entrada,))
x=0
while True:
    resultado=cursor.fetchone()
    if resultado == None:
        if x == 0:
            print("Produto não encontrado")
        break
    print("Nome do produto: %s\nPreço: %s" % resultado)
    x+=1

conexão.commit()
cursor.close()
conexão.close()