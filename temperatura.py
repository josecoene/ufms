t = float(input("Qual é a temperatura atual? "))

if t < 0.0:
    print("Está muito frio.")

if t >= 0.0 and t < 14.0:
    print("Está um pouco frio.")

if t >= 14.0 and t < 23.0:
    print("Está agradável.")

if t >= 23.0:
    print("Está calor.")
