def parImpar(numero):

    if numero % 2 == 0:
        return True
    else:
        return False


a = int(input("Digite um numero: "))
if parImpar(a) == True:
    print("Par")

else:
    print("Impar")