def main():
    while True:
        try:
            texto = input()
            resultadoFinal = ""
            comeco = 0
            fim = 0
            
            for i in range(len(texto)):
                if texto[i] == "_":
                    if comeco == 0:
                        resultadoFinal += "<i>"
                        comeco = 1
                    else:
                        resultadoFinal += "</i>"
                        comeco = 0
                elif texto[i] == "*":
                    if fim == 0:
                        resultadoFinal += "<b>"
                        fim = 1
                    else:
                        resultadoFinal += "</b>"
                        fim = 0
                else:
                    resultadoFinal += texto[i]

            print(resultadoFinal)
        
        except EOFError:
            break

main()
