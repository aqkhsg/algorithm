import sys

numList = list(range(3))

for i in range(3):
    numList[i] = int(sys.stdin.readline())

result = numList[0] * numList[1] * numList[2]

resultList = list(str(result))
intList = list(range(10))
for i in intList:
    print(resultList.count(str(i)))