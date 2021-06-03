n = int(input())

i = 0
res = 0
while i <= n:
    num = int(input())
    i += 1
    if i <= num:
        i += 1
        res = i
                     
print(i)