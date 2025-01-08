import random
n=random.randint(1,10)
for caractere in range(3):
    x = int(input("Escolha um número entre 1 e 10:"))
    if x==n:
        print("Você acertou!")
        break
    else:
        print("Você errou.")