def substituir(texto, verificacao, verificacao2, resultado):
    resultado = ""
    for i in range(len(texto)):
        if texto[i] == "_":
            if verificacao == 0:
                resultado += "<i>"
                verificacao = 1
            
            else:
                resultado += "</i>"
                verificacao = 0
        elif texto[i] == "*":     
            if verificacao2 == 0:
                resultado += "<b>"
                verificacao2 = 1
            
            else:
                resultado += "</b>"
                verificacao = 0
        else:
                resultado += texto[i]
    print(resultado)

def bloggo(texto):
    fim = ""
    verificar1 = 0
    verificar2 = 0

    substituir(texto, verificar1, verificar2, fim)

def main():
    while True:
        try:
            texto = input()
            bloggo(texto)
        except EOFError:
            break
main()
