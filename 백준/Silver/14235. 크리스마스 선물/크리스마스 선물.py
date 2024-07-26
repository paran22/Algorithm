# https://www.acmicpc.net/problem/14235

import sys
import heapq

n = int(sys.stdin.readline().strip())
heap = []
heapq.heapify(heap)

for _ in range(n):
    num = sys.stdin.readline().strip()
    if num == "0":
        answer = -heapq.heappop(heap) if len(heap) > 0 else -1
        print(answer)
    else:
        gifts = list(map(int, num.split()))[1::]
        for i in range(len(gifts)):
            heapq.heappush(heap, -gifts[i])
