lanche, quantidade = map(int, input().split())

if lanche == 1:
    print(f"Total: R$ {4.00 * quantidade:.2f}")
elif lanche == 2:
    print(f"Total: R$ {4.50 * quantidade:.2f}")
elif lanche == 3:
    print(f"Total: R$ {5.00 * quantidade:.2f}")
elif lanche == 4:
    print(f"Total: R$ {2.00 * quantidade:.2f}")
elif lanche == 5:
    print(f"Total: R$ {1.50 * quantidade:.2f}")
