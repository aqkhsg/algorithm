import sys

n=int(sys.stdin.readline())
scoreList = list(map(int, sys.stdin.readline().split()))
maxScore = max(scoreList)
newScoreSum=0
for i in scoreList:
    newScore = i/maxScore*100
    newScoreSum = newScoreSum+newScore
print(newScoreSum/n)