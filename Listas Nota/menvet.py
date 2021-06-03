tamanho = int(input())
vetor = input().split()

for i in range(len(vetor)):
    vetor[i] = int(vetor[i])

menorValor = vetor[0]
posicao = 0
for i in range(1, len(vetor)):
    if vetor[i] < menorValor:
        menorValor = vetor[i]
        posicao = i

print(f'Menor valor: {menorValor}')