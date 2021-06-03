def calculoPi(numero):

    pi = 0
    soma = True
    for i in range(1, num+1, 2):
        if soma:
            pi += 4 / i
            soma = False
        else:
            pi -= 4 / i
            soma = True
    
    print(f"{pi:.4f}")

num = int(input())
calculoPi(num)
