valido = True
valido2 = True
media = 0
while valido == True:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    elif nota >= 0 and nota <= 10:        

        while valido2 == True:
            nota2 = float(input())
            if nota2 < 0 or nota2 > 10:
                print("nota invalida")
            elif nota2 >= 0 and nota2 <= 10:
                media = (nota + nota2) / 2
                print(f"media = {media:.2f}")
                valido2 = False
        valido = False
