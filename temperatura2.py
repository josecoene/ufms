t = float(input("Qual é a temperatura atual? "))

if t < 0.0:
    print("Está frio.")
else:
    if t >= 0.0 and t < 14.0:
        print("Está pouco frio.")
    else:
        if t >= 14.0 and t < 23.0:
            print("Está agradáve.l")
        else:
            print("Está calor.")