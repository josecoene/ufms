num = int(input())

i = 2
primo = True
while i < num:
    if num % i == 0:
        primo = False

    i += 1
if primo:
    print("Primo")
else:
    print("Composto")
    