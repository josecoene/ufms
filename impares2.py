x = int(input())

i = 1
imp = 1
while i <= x:
    if imp % 2 != 0:
        imp = imp + i
        i += 1
        print(imp)