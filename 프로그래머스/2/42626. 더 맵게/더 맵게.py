import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        new = 0
        if scoville:
            new += heapq.heappop(scoville)
        else:
            return -1
        if scoville:
            new += heapq.heappop(scoville) * 2
        else:
            return -1
        heapq.heappush(scoville, new)
        count += 1
    return count