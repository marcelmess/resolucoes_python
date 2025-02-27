import random

lista_de_palavras = ["arroz", "feijão", "macarrão", "salmão", "tomate", "batata"]
random.shuffle(lista_de_palavras)
palavra = lista_de_palavras[0]
for x in range(20):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha=""
    for letra in palavra:
        senha +=letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
            if erros == 6:
                break
if erros == 6:
    print("Enforcado!")
    print(f"A palavra secreta era: {palavra}")