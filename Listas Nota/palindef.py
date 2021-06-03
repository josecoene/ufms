def isPalindrome(f):
    l = list(f)

    j = len(l) - 1
    for i in range(0, len(l) // 2):
        if l[i] != l[j]:
            return False
        j -= 1

    return True

def main():
    frase = input("Digite algo: ")

    if isPalindrome(frase):
        print("SIM")
    else:
        print("NAO")

main()