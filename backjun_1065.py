def CheckHan(num):
    if num < 100:
        return 1
    elif num <= 1000:
        numList = list(str(num))
        dif1 = int(numList[2]) - int(numList[1])
        dif2 = int(numList[1]) - int(numList[0])
        if dif1 == dif2:
            return 1
        return 0
n=int(input())
hanCount=0
for i in range(1,n+1):
    if(CheckHan(i)):
        hanCount = hanCount+1

print(hanCount)
