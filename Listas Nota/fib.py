n = int(input())

i = 2
anterior = 0
atual = 1
prox = 1

if n == 0:
    print("0")

elif n == 1:
    print("1")

else:
    while i <= n:
        i += 1
        prox = anterior + atual
        anterior = atual
        atual = prox
    
    print(f"{prox}")
