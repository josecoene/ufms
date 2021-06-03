a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

par = imp = pos = neg = 0



if a % 2 == 0:
    par += 1
elif a % 2 != 0:
    imp += 1

if a > 0:
    pos += 1
elif a < 0:
    neg += 1

if b % 2 == 0:
    par += 1
elif b % 2 != 0:
    imp += 1

if b > 0:
    pos += 1
elif b < 0:
    neg += 1

if c % 2 == 0:
    par += 1
elif c % 2 != 0:
    imp += 1

if c > 0:
    pos += 1
elif c < 0:
    neg += 1

if d % 2 == 0:
    par += 1
elif d % 2 != 0:
    imp += 1

if d > 0:
    pos += 1
elif d < 0:
    neg += 1

if e % 2 == 0:
    par += 1
elif e % 2 != 0:
    imp += 1

if e > 0:
    pos += 1
elif e < 0:
    neg += 1


print (f"{par} valor(es) par(es)\n{imp} valor(es) impar(es)\n{pos} valor(es) positivo(s)\n{neg} valor(es) negativo(s)")
