a, b, c = map(float, input().split())

tempa = tempb = tempc = 0

if c <= a >= b:
        tempa = a
        tempb = b
        tempc = c
elif c <= b >= a:
        tempa = b
        tempb = a
        tempc = c
elif a <= c >= b:
        tempa = c
        tempb = a
        tempc = b
        
if tempa < tempb + tempc:
        if tempa ** 2 == tempb ** 2 + tempc ** 2:
                print("TRIANGULO RETANGULO")
        elif tempa ** 2 > tempb ** 2 + tempc ** 2:
                print("TRIANGULO OBTUSANGULO")
        else:
                print("TRIANGULO ACUTANGULO")
        if tempa == tempb and tempb == tempc:
                print("TRIANGULO EQUILATERO")
        elif tempa == tempb or tempb == tempc or tempc == tempa:
                print("TRIANGULO ISOSCELES")
else:
        print("NAO FORMA TRIANGULO")
