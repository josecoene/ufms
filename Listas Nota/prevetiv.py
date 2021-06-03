def imprimir(tipo, lista, posicao):
    for posicao in range(len(lista)):
        print(f'{tipo}[{posicao}] = {lista[posicao]}')             

par = list()
impar = list()
i = list()
for i in range(0, 15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
        if len(par) == 5:
            for i in range(len(par)):
                imprimir("par", par, i)            
                par = []


    if x % 2 != 0:
        impar.append(x)
        if len(impar) == 5:
            for i in range(len(impar)):
                imprimir("impar", impar, i)
                impar = []

imprimir("impar", impar, i)
imprimir("par", par, i)
