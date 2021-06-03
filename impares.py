num = int(input())

i = 0
somapar = somaimp = 0 

while i < num:
    x = int(input())

    if x % 2 == 0:
        somapar = somapar + x
    else:
        somaimp = somaimp + x
    i = i + 1
print(f"Pares: {somapar}\nImpares: {somaimp}")