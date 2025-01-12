import time
tempo1 = time.localtime()
lista_de_palavras = ["arroz", "feijão", "macarrão", "salmão", "tomate", "batata"]
entrada = int(input("Digite um número:"))
índice = (entrada * 776) % len(lista_de_palavras)
palavra = lista_de_palavras[índice]
for x in range(100):
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
tempo2=time.localtime()
diferença = tempo2.tm_sec - tempo1.tm_sec
print(f"Levou {diferença} segundos para resolver")