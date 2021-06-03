def somador(x, y, soma):
    excedente = 0

    for i in range(len(x) - 1, -1, -1):

        if excedente == 0:
            soma_n = x[i] + y[i]
        else:
            soma_n = x[i] + y[i] + excedente
            excedente -= 1

        if soma_n >= 10:
            excedente += 1
            soma_n -= 10
            soma.append(soma_n)
        else:
            soma.append(soma_n)

        if i == 0 and excedente == 1:
            soma.append(excedente)


def imprime(soma):
    for numero in range(len(soma) - 1, -1, -1):
        print(soma[numero], end=' ')


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    soma = list()

    somador(a, b, soma)

    imprime(soma)


main()