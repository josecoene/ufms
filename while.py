import random

n = random.randint (0, 5)
acertou = True

while acertou:
    i = int(input("Adivinhe o numero."))
    if i == n:
        print("Voce acertou!")
        acertou = False
    else:
        print("Voce errou! Tente novamente")
print("Bye!")