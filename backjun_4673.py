def d(a):
    numListStr = list(str(a))
    sum=a
    for i in numListStr:
        sum = sum + int(i)
    return sum

numSet = set(range(1,10001))
notSelfNumSet = set()
for i in numSet:
    notSelfNumSet.add(d(i))

for i in numSet:
    if i in notSelfNumSet:
        pass
    else:
        print(i)