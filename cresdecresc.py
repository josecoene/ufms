i = 0
prog = True
while prog == True:
    x, y = map(int, input().split())
    if x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
    elif x == y:
        prog = False
