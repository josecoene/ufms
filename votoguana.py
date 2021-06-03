def voto(anoNasc):
    if anoNasc > 2002:
        print("Voto negado")
    elif anoNasc == 2002:
        print("Voto Opcional")
    else:
        print("Voto Obrigatorio")


ano = int(input("Digite o ano de seu nascimento: "))
voto(ano)