n = int(input())

if n > 0:
    print(f"{n} é positivo.")
    if n >= 1000000:
        print(f"{n} é um numero alto.")
    else:
        print(f"{n} é um numero baixo.")
else:
    print(f"{n} é não positivo.")
