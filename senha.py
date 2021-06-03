def main():
    acesso = True
    while acesso == True:
        senha = int(input())
        if senha != 2002:
            print("Senha invalida")
        else:
            print("Acesso permitido")
            acesso = False
    return senha

main()