ano = int(input())

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("Bissexto")
        else:
            print("Ano qualquer")
    else:
        print("Bissexto")
else:
    print("Ano qualquer")