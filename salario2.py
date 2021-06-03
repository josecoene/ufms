nome = input()
salario = float(input())
vendas = float(input())

bonus = 15 * (vendas / 100)

total = salario + bonus

print(f"TOTAL = R$ {total:.2f}")