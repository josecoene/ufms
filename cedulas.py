valor = int(input())

cedulas_100 = valor // 100

cedulas_50 = valor - cedulas_100 * 100
notas_50 = cedulas_50 // 50

cedulas_20 = valor - cedulas_100 * 100 - notas_50 * 50
notas_20 = cedulas_20 // 20

cedulas_10 = valor - cedulas_100 * 100 - notas_50 * 50 - notas_20 * 20
notas_10 = cedulas_10 // 10

cedulas_5 = valor - cedulas_100 * 100 - notas_50 * 50 - notas_20 * 20 - notas_10 * 10
notas_5 = cedulas_5 // 5

cedulas_2 = valor - cedulas_100 * 100 - notas_50 * 50 - notas_20 * 20 - notas_10 * 10 - notas_5 * 5
notas_2 = cedulas_2 // 2

cedulas_1 = valor - cedulas_100 * 100 - notas_50 * 50 - notas_20 * 20 - notas_10 * 10 - notas_5 * 5 - notas_2 * 2
notas_1 = cedulas_1 // 1

print(f"{valor}")
print(f"{cedulas_100} nota(s) de R$ 100,00")
print(f"{notas_50} nota(s) de R$ 50.00")
print(f"{notas_20} nota(s) de R$ 20,00")
print(f"{notas_10} nota(s) de R$ 10,00")
print(f"{notas_5} nota(s) de R$ 5,00")
print(f"{notas_2} nota(s) de R$ 2,00")
print(f"{notas_1} nota(s) de R$ 1,00")