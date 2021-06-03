def lerEntrada(vet):
    vet = []
    for i in range(20):
        num = int(input())
        vet.append(num)

def substituirVet(vet):
    for i in range(10):
        if vet[i] <= 0:
            vet[i] = 1

def printVet(vet):
    for i in range(0, len(vet[i])):
        print(f'X[{i}] = {vet[i]}')

def main():
    vet = []
    lerEntrada(vet)
    substituirVet(vet)
    printVet(vet)

main()