def continha(a, b, resultado):
    
    passar = 0
    num = 0
    for i in range(len(a) - 1, -1, -1):
        if passar == 0:
            num = a[i] + b[i]
        else:
            num = a[i] + b[i]
            num += passar
            passar -= 1

        if num >= 10:
            passar += 1
            num -= 10
            resultado.append(num)
        else:
            resultado.append(num)
        if i == 0 and passar == 1:
            resultado.append(passar)
    for num in range(len(resultado) - 1, -1, -1):
        print(resultado[num], end=" ")

def main():
    sequenciaA = list(map(int, input().split()))
    sequenciaB = list(map(int, input().split()))
    resultado = list()
    continha(sequenciaA, sequenciaB, resultado)
 
main()
