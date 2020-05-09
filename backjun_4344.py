import sys

n = int(input())

for k in range(n):
    inputList = list(map(int,input().split()))
    cnt = inputList.pop(0)
    sumScore=0
    for i in inputList:
        sumScore += i
    mean = sumScore/cnt
    
    overCnt=0
    for i in inputList:
        if i > mean:
            overCnt +=1

    print('%.3f'%(overCnt/cnt * 100) + '%' )

