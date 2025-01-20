import sqlite3

dados = [("Macarrão", "5,99"), ("Arroz 1kg", "18,99"), ("Picanha", "34,87")]

conexão = sqlite3.connect("preços.db")
cursor = conexão.cursor()
cursor.execute("create table preços(nome text, preço text)")
cursor.executemany("insert into preços(nome, preço) values (?, ?)", dados)

conexão.commit()
cursor.close()
conexão.close()