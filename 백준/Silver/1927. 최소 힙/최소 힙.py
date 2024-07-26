# https://www.acmicpc.net/problem/1927

import sys
import heapq

N = int(sys.stdin.readline().strip())
heap = []
heapq.heapify(heap)

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        min_heap = heapq.heappop(heap) if len(heap) > 0 else 0
        print(min_heap)
    else:
        heapq.heappush(heap, num)
