n = int(input())

top = anterior = cresc = 0
c = 0

while c < n:
    n = int(input())

    if c == 0:
        anterior = n
        top = cresc = 1

    else:
        if n > anterior:
            anterior = n
            top += 1
            cresc = top
        else:
            anterior = n
            if cresc > top:
                top = 1
            else:
                cresc = top
                top = 1
    c += 1
print(top)