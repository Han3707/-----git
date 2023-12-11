num = ['0','1','2','3','4','5','6','7','8','9']
sums = 0
sumstr =[]
s = input()

for i in s:
    if i in num:
        sums += int(i)
    else:
        sumstr.append(i)
sumstr.sort()

sumstr.append(str(sums))

print(''.join(sumstr))

print('a')

