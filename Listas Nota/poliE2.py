def somarPolinomios(polinomios):
    quantInteiro = int(input())

    while quantInteiro > 0:
        reais = float(input())
        somaPolinomio = 0

        for n in range(0, len(polinomios)):
            somaPolinomio = somaPolinomio + (polinomios[n] * (reais ** n))
        
        print(f"{somaPolinomio:.4f}")
        quantInteiro -= 1

def lerVetor():
    vetor = list(map(float, input().split()))
    return vetor

def main():
    valores = lerVetor()
    somarPolinomios(valores)

main()