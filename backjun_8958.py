import sys

n = int(input())

for k in range(n):
    quizResult=list(sys.stdin.readline())
    score=0
    sum=0
    for i in quizResult:
        if i=='O':
         score= score+1
         sum = sum + score
        if i=='X':
         score =0
    print(sum)
    quizResult.clear()