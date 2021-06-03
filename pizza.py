tamanho, queijo, borda = (input().split())

total = 0

if tamanho == "P":
    total = 15.00
elif tamanho == "M":
    total = 18.50
else:
    total = 23.00

if queijo == "S":
    if tamanho == "P":
        total = total + 2.50
    else:
        total = total + 4.00
else:
    total = total + 0

if borda == "S":
    total = total + 5.00
else:
    total = total + 0

print(f"Total: R$ {total:.2f}")
