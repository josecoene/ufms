lanche, quantidade = map(int, input("Digite o código do lanche e a quantidade desejada: ").split())

if lanche == 1:
    print(f"Total: R$ {4.00 * quantidade:.2f}")
else:
    if lanche == 2:
        print(f"Total: R$ {4.50 * quantidade:.2f}")
    else:
        if lanche == 3:
            print(f"Total: R$ {5.00 * quantidade:.2f}")
        else:
            if lanche == 4:
                print(f"Total: R$ {2.00 * quantidade:.2f}")
            else:            
                if lanche == 5:
                    print(f"Total: R$ {1.50 * quantidade:.2f}")

lanche, quantidade = map(int, input("Algo mais? ").split())

if lanche == 1:
    print(f"Total: R$ {4.00 * quantidade:.2f}")
else:
    if lanche == 2:
        print(f"Total: R$ {4.50 * quantidade:.2f}")
    else:
        if lanche == 3:
            print(f"Total: R$ {5.00 * quantidade:.2f}")
        else:
            if lanche == 4:
                print(f"Total: R$ {2.00 * quantidade:.2f}")
            else:            
                if lanche == 5:
                    print(f"Total: R$ {1.50 * quantidade:.2f}")

satisfeito = input("Satisfeito? Responda com 's' ou 'n'. ")

if satisfeito == "s":
    print("Obrigado pela preferência!")
if satisfeito == "n":
    print("Envie-nos sua avaliação no nosso site: 'link aqui'.")