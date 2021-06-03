def imprime(posicao):
    if len(posicao) == 0:
        print("NOT FOUND!")
    else:
        for num in posicao:
            print(num)

def main():    
    frase = input()
    palavra = input()
    posicao = []

    for i in range(len(frase)):
        pos = i + len(palavra)
        if frase[i:pos] == palavra:
            posicao.append(i)
    imprime(posicao)

main()
