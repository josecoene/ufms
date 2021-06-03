def lerVetor():
    vetor = list(map(float, input().split()))
    return vetor

def variaveis():
    u = lerVetor()
    v = lerVetor()
    contador = soma = 0

    while  contador < len(u):
        produto = u[contador] * v[contador]
        soma += produto
        contador += 1
    
    print(f"{soma:.4f}")
    
def main():
    variaveis()


main()