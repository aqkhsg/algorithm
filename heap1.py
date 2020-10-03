import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while True:
        minSco = hq.heappop(scoville)
        if minSco < K:
            answer +=1
            secondMinSco = hq.heappop(scoville)
            mixSco = minSco + secondMinSco*2
            hq.heappush(scoville,mixSco)
        else:
            if len(scoville) == 0:
                return -1
            else:
                break
    return answer

a = solution([1, 2, 3, 9, 10, 12],7)
print(a)