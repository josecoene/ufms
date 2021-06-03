def maiorElemento(x):
    maior = x[0]
    for i in range(1, len(x)):
        if x[i] > maior:
            maior = x[i]
    return maior

def menorElemento(x):
    menor = x[0]
    for i in range(1, len(x)):
        if x[i] < menor:
            menor = x[i]
    return menor

def mediaElementos(x):
    soma = 0
    for i in x:
      soma += i
    return soma / len(x)  


def main():
    x = list(map(float, input().split()))
    
    maiorx = maiorElemento(x)
    print(f'O maior elemento da lista é {maiorx:.2f}.')

    menorx = menorElemento(x)
    print(f'O menor elemento da lista é {menorx:.2f}.')

    mediax = mediaElementos(x)
    print(f'A media dos elementos é {mediax:.2f}.')

main()