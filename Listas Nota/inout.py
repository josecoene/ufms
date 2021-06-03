qtdTeste = int(input())

for i in range(qtdTeste):
    testes = input()
    alt = list(int(len(testes)/2) - 1)
    sair = testes[alt] + testes
print(sair)